
co = 0 

while num != 0:
    if num % 2 == 0:
        num = num // 2
    else:
        num -= 1
    co += 1 

print(co)
