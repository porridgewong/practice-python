import os
import time
from contextlib import contextmanager


@contextmanager
def timer():
    """Context manager that measures the time of the block execution."""
    start = time.time()
    try:
        yield
    finally:
        print(f"Elapsed time: {time.time() - start}")


@contextmanager
def set_temporary_env(**kwargs):
    """Context manager that temporarily sets the environment variables for the block execution."""
    to_remove = set()
    original = {}
    for key, value in kwargs.items():
        if key not in os.environ:
            to_remove.add(key)
        else:
            original[key] = os.environ[key]
        os.environ[key] = value
    try:
        yield
    finally:
        for key in to_remove:
            del os.environ[key]
        for key, value in original.items():
            os.environ[key] = value


def main() -> None:
    with timer():
        time.sleep(1)

    print(os.environ.get("TEST"))
    with set_temporary_env(TEST="test"):
        print(os.environ.get("TEST"))
    print(os.environ.get("TEST"))


main()
