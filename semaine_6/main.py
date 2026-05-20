import lib as im

def bar(y: int):
    print("Hello bar")
    return im.foo(y) + 1

print(bar(5))