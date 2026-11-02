#1
#טהור
#לא טהור
#לא טהור
#טהור



# 2
# total = 20
# def add_price(total, price):
#     new_total = total
#     new_total += price
#     return new_total
#
# print(add_price(total, 10))
# print(add_price(total, 10))
# print(total)



# 3
# TAX = 1.17
# def apply_tax(prices):
#     full_price = []
#     for i in range(len(prices)):
#         full_price.append(prices[i] * TAX)
#     return full_price
#
# prices = [100 , 50]
# with_tax = apply_tax(prices)
# print(prices)
# print(with_tax)



# 4
# def calculate_total(prices):
#     end_total = 0
#     for price in prices:
#         end_total += price
#     return end_total
#
# def show_total(prices):
#     print(calculate_total(prices))
#
#
# total = [10, 40]
# show_total([10,20,30])
# print(total)



5
def top_three(numbers):
    sorted_numbers = sorted(numbers, reverse= True)
    return sorted_numbers[:3]
scores = [70, 95, 88, 60, 99]
print(top_three(scores))
print(scores)



