from contextlib import contextmanager


class TestOpen:
    def __init__(self, file_path):
        print("init")
        self.file_path = file_path

    def __enter__(self):
        print("enter")
        return self.file_path

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("exit")
        if exc_type is ValueError:
            print(f"Caught an exception: {exc_value} {exc_tb}")
            return True


@contextmanager
def test_open(file_path):
    print("enter")
    try:
        yield file_path
    finally:
        print("exit")


def main():
    print("class context manager")
    with TestOpen("test.txt") as file_path:
        raise ValueError("test error")
    print("file_path:", file_path)

    print("function context manager")
    with test_open("test.txt") as file_path:
        print("file_path:", file_path)


main()
