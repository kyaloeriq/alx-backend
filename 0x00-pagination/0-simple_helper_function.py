#!/usr/bin/env python3
"""
Module providing pagination helper functions.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start and end index for pagination
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
