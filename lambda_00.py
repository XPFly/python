def square_fn(x):
    return x * x

# print(square_fn(2))

square_ld = lambda x: x * x

for i in range(10):
    assert square_fn(i) == square_ld(i)

square_fn(2)
square_ld(2)