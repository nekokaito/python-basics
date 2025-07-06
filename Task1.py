# Print numbers 1 to 10 using a loop.

# Print even numbers from 1 to 100.

# Print all characters of a given string.

# Calculate the sum of all numbers from 1 to N (input).

# Print the multiplication table of a given number (e.g., 5).

# Reverse a given string using a loop.

# Count the number of vowels in a string.

# Find the factorial of a number using a loop.

# Print all elements of a list.

# Print only the positive numbers from a list.


#Task 1

for i in range(1,11):
     print(i)
     
#Task 2     
for i in range(1,101):
    i%2 == 0 and print(i)

#Task 3

y = "Kaito"

for i in y:
     print(i)

#Task 4  

n = 51
sum = 0
for i in range(n):
     sum = sum+i
     
print(sum)

#Task 5


h = 5

for i in range(1,11):
     print(f"{h} x {i} = {h*i}")
     
#Task 6

lm = "Nikkaa"
sm = ""

for i in range(len(lm)):
      sm = lm[len(lm) - 1 - i]
      print(sm, end="")

# Another Way
for i in reversed(lm):
     print(i)


     