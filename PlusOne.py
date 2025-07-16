number = [2, 2, 3]


result = int(''.join(str(n) for n in number))
lists = [int(digit) for digit in str(result+1)]

print(lists)