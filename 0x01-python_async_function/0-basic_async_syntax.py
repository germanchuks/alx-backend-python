#!/usr/bin/env python3
"""Takes in an integer argument `max_delay` and waits for a random delay
between 0 and max_delay seconds and eventually returns it."""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Returns random delay between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
