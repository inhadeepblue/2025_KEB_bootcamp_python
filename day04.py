# v3.9
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Function Name : {func.__name__}')
        print(f'Function Arguments : {args}')
        print(f'Function Keyword Arguments : {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper


@log_decorator
def greet(name, greeting="안녕하세요", age=None):
    return f"{greeting}, {name}(age: {age})" if age else f"{greeting}, {name}"

print(greet("인하"))
print(greet("인상", "안녕"))
#print(greet("James", "Hello"))
print(greet("Gonzales", greeting="Hola"))
print(greet("Nakamura", greeting="Gonniziwa", age=29))
