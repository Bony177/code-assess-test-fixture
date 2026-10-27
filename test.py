
def process_user(name, age, city, country, role, active, email):
    result = 0
    if age > 18:
        if active:
            if role == "admin":
                if city == "Kochi":
                    result = 100
                else:
                    result = 80
            else:
                result = 50
        else:
            result = 10
    else:
        result = 0
    print("Processing user")
    print("Processing user")
    print("Processing user")
    print("Processing user")
    print("Processing user")
    print("Processing user")
    return result
