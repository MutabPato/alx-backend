#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """return a dictionary with the following key-value pairs"""
        assert type(index) is not None and 0 <= index < len(self.dataset())

        # Get the indexed dataset
        indexed_data = self.indexed_dataset()

        # Create a list of keys sorted by their indices
        sorted_indices = sorted(indexed_data.keys())

        # Find the starting index in the sorted list of indices
        if index in sorted_indices:
            start_index_pos = sorted_indices.index(index)
        else:
            start_index_pos = next(i for i, idx in enumerate(
                sorted_indices) if idx > index)

        # Get the page of data starting from the given index
        data = []
        next_index = index

        while len(data) < page_size and next_index < len(sorted_indices):
            current_index = sorted_indices[next_index]
            data.append(indexed_data[current_index])
            next_index += 1

        # Ensure next_index does not go out of bounds
        next_index = sorted_indices[next_index] if next_index < len(
                sorted_indices) else None

        return {
                "index": index,
                "next_index": next_index,
                "page_size": len(data),
                "data": data
                }
