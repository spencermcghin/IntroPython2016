#!/usr/bin/env python3

"""
timing context manager
"""

import time


class Timer:

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Elapsed Time:", time.time() - self.start)
