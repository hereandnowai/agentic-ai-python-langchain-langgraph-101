numbers = [1, 2, 3, 4, 5, 6]

evens_loop = []
for number in numbers:
    if number % 2 == 0:
        evens_loop.append(number)
print(f"evens using loop: {evens_loop}")

evens_comp = [n for n in numbers if n % 2 == 0]
print(f"evens using comprehension: {evens_comp}")