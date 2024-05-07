#!/usr/bin/env python3
"""
Collects 10 random numbers using an async comprehension and returns the 10
random numbers.
"""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Returns 10 random numbers using async comprehension"""
    return [num async for num in async_generator()]
