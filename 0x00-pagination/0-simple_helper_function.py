#!/usr/bin/env python3
"""Define index_range function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the index of page content"""
    return (page_size * (page - 1), page_size * page)
