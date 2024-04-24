import random

from runtime_params import MIN_REQUEST_DELAY, MAX_REQUEST_DELAY


def random_delay() -> int:
    return random.randint(MIN_REQUEST_DELAY, MAX_REQUEST_DELAY)
