def is_prime(func):
    def wrapper(*args):
        sum_ = func(*args)

        if isinstance(sum_, int):
            print("Простое")
        else:
            print("Составное")

        return sum_

    return wrapper

@is_prime
def sum_three(*nums):
    return sum(nums)

result = sum_three(2, 3, 6)
print(result)