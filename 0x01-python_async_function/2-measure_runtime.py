#!/usr/bin/env python3
""" Measure runtime module """
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    Returns total time / n
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n

    return total_time
