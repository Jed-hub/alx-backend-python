#!/usr/bin/env python3
""" tasks module """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Retuns a asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
