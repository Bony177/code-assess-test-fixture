
"""Synthetic CODE//ASSESS test fixture. All credentials are fake."""

FAKE_API_KEY = "FAKE_TEST_KEY_DO_NOT_USE_12345"


def add(a, b):
    """A simple low-complexity function."""
    return a + b


def calculate_discount(price, customer_type, is_member, has_coupon, region, order_count, is_holiday, payment_method):
    """Intentionally many parameters and several decision paths."""
    discount = 0
    if customer_type == "student":
        discount += 10
    elif customer_type == "senior":
        discount += 15
    else:
        discount += 2
    if is_member:
        discount += 5
    if has_coupon and price > 100:
        discount += 8
    if region == "north" or region == "west":
        discount += 3
    if order_count > 10:
        discount += 4
    if is_holiday:
        discount += 6
    if payment_method == "cash":
        discount += 1
    final_price = price * (1 - discount / 100)
    if final_price < 0:
        return 0
    return round(final_price, 2)


def process_orders(orders):
    """Intentionally long-ish function with nested branches."""
    results = []
    for order in orders:
        if not order:
            continue
        if "price" not in order:
            results.append({"status": "invalid", "reason": "missing price"})
            continue
        price = order["price"]
        if price <= 0:
            results.append({"status": "invalid", "reason": "bad price"})
        else:
            if order.get("paid"):
                if order.get("in_stock"):
                    results.append({"status": "accepted", "total": price})
                else:
                    results.append({"status": "waiting", "total": price})
            else:
                results.append({"status": "unpaid", "total": price})
    return results


def is_even(number):
    return number % 2 == 0


if __name__ == "__main__":
    sample_orders = [
        {"price": 25, "paid": True, "in_stock": True},
        {"price": 50, "paid": False, "in_stock": True},
        {"price": -5, "paid": True, "in_stock": False},
        {},
    ]
    print("add:", add(2, 3))
    print("discount:", calculate_discount(150, "student", True, True, "north", 12, False, "cash"))
    print("orders:", process_orders(sample_orders))
    print("even:", is_even(4))
