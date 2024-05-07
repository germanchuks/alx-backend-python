#!/usr/bin/env python3
"""
Executes async_comprehension four times in parallel using asyncio.gather
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures and returns the total runtime of executing async_comprehension
    four times in parallel."""
    start_time = time.perf_counter()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    total_time = time.perf_counter() - start_time

    return total_time
