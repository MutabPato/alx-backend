#!/usr/bin/env python3
"""Pagination"""


import csv
import math
from typing import List


def index_range(page, page_size):
    """ return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters"""
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
        """takes two integer arguments and
        return the appropriate page of the dataset"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        (start_index, end_index) = index_range(page, page_size)
        data = self.dataset()
        paginated_data = data[start_index:end_index]
        return paginated_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns a dictionary containing the following key-value pairs"""

        paginated_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
                "page_size": len(paginated_data),
                "page": page,
                "data": paginated_data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
