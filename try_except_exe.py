1
def to_number(text):
    try:
        return int(text)
    except ValueError:
        return f"{text} is not a number"

print(to_number("4"))
print(to_number("ghfgf"))
print(to_number("-4"))



2
def safe_divide(text1, text2):
    try:
        return int(text1) / int(text2)
    except ValueError:
        return "numbers only"
    except ZeroDivisionError:
        return  "cannot divide by zero"

print(safe_divide("10", "4"))
print(safe_divide("10", "0"))
print(safe_divide("10", "gfd"))



3
try:
    number = int("12asdf")
except ValueError as error:
    print(f"Could not convert: {error}")



4
def pick(names, position_text):
    try:
        return names[int(position_text)-1]
    except ValueError:
        return "not a number"
    except IndexError:
        return "no such position"

print(pick(["hgfd" , "r" , "w"] , "2"))
print(pick(["hgfd" , "r" , "w"] , "g"))
print(pick(["hgfd" , "r" , "w"] , "10"))




