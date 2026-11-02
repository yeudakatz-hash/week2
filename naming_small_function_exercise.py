1
TOTAL = 500
DISCOUNT = 50

def calculate_total(product, count):
    multiple = product * count
    if multiple > TOTAL:
        multiple -= DISCOUNT
    return multiple

#
#
# 2
# TotalPrice (a variable)                          YES
# numberofstudents (a variable)                    NO
# max_grade (a variable)                           YES
# vat_rate (a constant that never changes)         NO
# GetAverage (a function)                          YES
#
#

3
GRADE_PASS = 55
def calculate_average(grades):
    total = 0
    for g in grades:
        total = total + g
    avg = total / len(grades)
    return avg

def is_passing(cal_avg):
    if cal_avg > GRADE_PASS:
        report = "passed"
    else:
        report = "failed"
    return report

def print_report(name, grades):
    cal_avg = calculate_average(grades)
    passing = is_passing(cal_avg)
    print(name, cal_avg , passing)

print_report("yehuda" , grades=[0,0,100])



4
BIG_ORDER = 200
SMALL_ORDER_FEE = 30
def final_price(total):
    if total < BIG_ORDER:
        total = total + SMALL_ORDER_FEE
    return total
print(final_price(150))
print(final_price(250))



5
def is_valid_password(password):
    have_dig = False
    for char in password:
        if char in "0123456789":
            have_dig = True
    return have_dig and len(password) >= 8

print(is_valid_password("sdfgh4fj"))