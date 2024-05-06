#!/usr/bin/env python3
"""
Imports wait_random, takes 2 argument and spawn wait_random n times with
specified max_delay and return the list of all delays in ascending order.
"""
import asyncio
from typing import List
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of all delays in ascending order."""
    tasks: List[Task] = []
    delays: List[float] = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return sorted(delays)
