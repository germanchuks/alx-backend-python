#!/usr/bin/env python3
"""
Imports `wait_n`, takes 2 arguments (n and max_delay) and measures the total
execution time for wait_n and returns total_time / n.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures total execution time for wait_n and returns total_time / n"""
    start_time = time.perf_counter()

    await wait_n(n, max_delay)

    end_time = time.perf_counter()
    total_time = end_time - start_time

    return total_time / n
