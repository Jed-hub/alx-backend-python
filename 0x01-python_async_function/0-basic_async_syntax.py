#!/usr/bin/env python3
"""
Module
"""
import asyncio
import time
import random


async def wait_random(max_delay=10):
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
