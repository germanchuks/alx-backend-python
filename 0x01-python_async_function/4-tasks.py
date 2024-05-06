#!/usr/bin/env python3
"""
Takes the code from wait_n and alter it into a new function task_wait_n.
"""
import asyncio
from typing import List
from asyncio import Task

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of all delays in ascending order."""
    tasks: List[Task] = []
    delays: List[float] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return sorted(delays)
