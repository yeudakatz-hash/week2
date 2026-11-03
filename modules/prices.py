VAT_RATE = 0.17

def add_vat(amount):
    return amount * (1 + VAT_RATE)

def apply_discount(amount, percent):
    return amount * ((100 - percent) / 100)

