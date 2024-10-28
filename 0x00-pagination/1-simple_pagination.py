#!/usr/bin/env python3
"""Pagination"""

import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Simple helper function"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(
                page, int) and page > 0, "page must be an integer > 0"
        assert isinstance(
                page_size, int
                ) and page_size > 0, "page_size must be an integer > 0"
        data = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(data):
            return []

        return data[start:end]