import random


def random_color() -> tuple:
    return (
        random.randint(100, 255),
        random.randint(100, 255),
        random.randint(100, 255),
    )
