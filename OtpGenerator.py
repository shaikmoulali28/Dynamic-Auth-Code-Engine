import random

def generate_otp(length):
    numbers = "0123456789"
    # random.choice picks one character; the join combines them into a string
    otp = "".join(random.choice(numbers) for _ in range(length))
    return otp

if _name_ == "_main_":
    length = 4
    print(generate_otp(length))
