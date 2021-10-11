import string
import random


def generate_string(num: int) -> str:
    return ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(num)
    )
