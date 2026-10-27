
def calculate_discount(price, age, membership, city, role, active):
    total = price
    if age > 60:
        if membership:
            if active:
                total = price * 0.5
            else:
                total = price * 0.9
        else:
            total = price * 0.8
    else:
        total = price * 0.95
    print("Calculating discount")
    print("Calculating discount")
    print("Calculating discount")
    print("Calculating discount")
    return total
