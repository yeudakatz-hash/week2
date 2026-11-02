from itertools import count

from select import error

# 1
# def make_greeting(name, greeting = "Hello", punct = "!"):
#     return f"{greeting}, {name}{punct}"
#
# print(make_greeting("dana"))
# print(make_greeting("avi" , "good morning"))
# print(make_greeting("noa" , punct="?"))



# 2
# def average(*numbers):
#     count = 0
#     for i in numbers:
#         count += 1
#     return sum(numbers) / count
#
# try:
#     print(average(40))
# except ValueError as error:
#     print("error:", error)
# except ZeroDivisionError as error:
#     print("error:" , error)



#טעון בדיקה!!!3
# def format_profile(name, **details):
#     return f"{name}:, details"
#
# print(format_profile("avi", age = 24, city = "haifa" ))



#4
# products = [("laptop", 3500) , ("mouse", 80) , ("desk", 900)]
# sort_list = list(sorted(products, key =lambda p: p[1]))
# for item in sort_list:
#     print(*item)
#
# max_price = sort_list = list(max(products, key=lambda p: p[1]))
# print(f"Most expensive: {max_price[0]}")
