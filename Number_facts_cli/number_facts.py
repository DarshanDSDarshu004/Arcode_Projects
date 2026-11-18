
import math

def count_digits(n):
    n = abs(n)

    if n == 0:
        return 1

    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count


def digit_sum(n):
    n = abs(n)
    total = 0

    while n != 0:
        total += n % 10
        n //= 10

    return total


def print_divisors(n):
    res = []

    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)

    return res


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def main():
    n = int(input("Enter a number: "))

    print("Number of digits:", count_digits(n))
    print("Digit sum:", digit_sum(n))

    ans = print_divisors(n)

    print("Divisors:")
    for i in range(len(ans)):
        print(ans[i])

    print("Prime:", is_prime(n))


if __name__ == "__main__":
    main()
