

class WithSample:
    def __init__(self):
        self.sample = 0
        print(f"{self.__class__.__name__} init")

    def __enter__(self):
        print(f"{self.__class__.__name__} enter")
        self.sample += 1
        return  self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.__class__.__name__} exit")

    def do_something(self):
        print(f"{self.__class__.__name__} do something")

with WithSample() as ws:
    ws.do_something()