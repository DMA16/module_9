def is_prime(func):
    def wrapper(*args):
        sum_ = func(*args)

        if (0 < sum_ <= 3) or (sum_ % 2 != 0 and sum_ % 3 != 0):
            print("Простое")
        else:
            print("Составное")

        return sum_

    return wrapper

@is_prime
def sum_three(*nums):
    return sum(nums)

result = sum_three(3, 3, 6)
print(result)
