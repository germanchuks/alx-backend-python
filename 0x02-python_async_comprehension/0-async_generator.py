#!/usr/bin/env python3
"""
Loops 10 times, each time asynchronously wait 1 second, and yields a random
number between 0 and 10 using the random module.
"""
import random
import asyncio


async def async_generator():
    """Yields random numbers 10 times with 1second delay."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
