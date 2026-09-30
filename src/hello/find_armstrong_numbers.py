def findArmstrongNumbers(start: int, end: int) -> list:
    armstrong_numbers = []
    for num in range(max(start, 0), end + 1):
        digits = [int(d) for d in str(num)]
        num_digits = len(digits)
        if num == sum(d ** num_digits for d in digits):
            armstrong_numbers.append(num)
    return armstrong_numbers