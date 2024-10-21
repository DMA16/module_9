def is_prime(func):
    def wrapper(*args):
        sum_ = func(*args)
        divisor_counter = 0

        if sum_ < 2:
            print("Не является простым или составным числом")
        else:
            for i in range(1, sum_ + 1):
                if sum_ % i == 0:
                    divisor_counter += 1

                if divisor_counter > 2:
                    break

            if divisor_counter == 2:
                print("Простое")
            else:
                print("Составное")

        return sum_

    return wrapper

@is_prime
def sum_three(*nums):
    return sum(nums)

result = sum_three(49)
print(result)