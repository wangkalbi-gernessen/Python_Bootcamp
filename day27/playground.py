# def add(*args):
#     print(args[1])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(3,5,6,2,1,7))

# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=5, multiply=6)