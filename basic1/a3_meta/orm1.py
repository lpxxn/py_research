


class ModelMetaClass:
    def __new__(cls, *args, **kwargs):
        print(f'{cls.__name__} is being created')
        return super().__new__(cls, *args, **kwargs)