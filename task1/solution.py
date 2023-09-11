def strict(func):
    def wrapper(*args, **kwargs):
        list_ann = [v for k, v in func.__annotations__.items()][0:-1]
        for value, tp in zip(args, list_ann):
            if not isinstance(value, tp):
                return TypeError
        return func(*args)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b