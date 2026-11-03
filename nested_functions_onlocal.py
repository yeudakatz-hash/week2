# 1
# def format_receipt(items):
#     def line(name, price):
#         return name.ljust(10) + str(price)
#     lines = []
#     for name , price in items:
#         lines.append(line(name, price))
#     return "\n".join(lines)
#
# print(format_receipt([("milk", 6) , ("bread" , 3)]))

# 2
# def make_greeter(greeting):
#     def greet(name):
#         return f"{greeting}, {name}"
#     return greet
#
# hello = make_greeter("Hello")
# shalom = make_greeter("shalom")
# print(hello("Dana"))
# print(shalom("Avi"))



# 3
# def make_counter(step):
#     count = 0
#     def increment(step):
#         nonlocal count
#         count += step
#         return count
#     return increment
#
# by_ten = make_counter(10)
# by_two = make_counter(2)





