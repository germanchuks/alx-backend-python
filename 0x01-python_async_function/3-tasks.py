#!/usr/bin/env python3
"""Imports wait_random, takes an integer argument max_delay and returns a
asyncio.Task"""
import asyncio
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Returns an asyncio.Task to execute wait_random"""
    return asyncio.create_task(wait_random(max_delay))
