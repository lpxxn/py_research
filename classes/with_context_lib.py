
import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print(f"open file: {file_name}") ## like __enter__
    yield {}
    print(f"close file: {file_name}") ## like __exit__


with file_open("test.txt") as f:
    print(f)
    print("file procession")