# === for loop ===
# here i is called loop counter and 10 is the number of times that the loop will execute
# The range() is a built-in function in python
# The range(n) generates a sequence of n integers starting at zero.
# It increases the value by one until it reaches n.
for i in range(10):
    print(i)

# We can also specify the starting value of range
for i in range(1, 11):
    print(i)

# We can also specify the increament sequence
for i in range(1, 11, 2):
    print(i)

# break in for loop

for i in range(50, 60):
    print(i)
    if i == 55:
        break

# continue in for loop
for i in range(0, 10):
    if i % 2:
        continue
    print(i)


# === while loop ===
max = 5
counter = 0
while counter < max:
    print(counter)
    counter += 1

# break in while loop

c = 0
while True:
    print(c)
    c += 1
    if c == 5:
        break

# continue in while loop
num = 0
while num < 10:
    num += 1
    if not num % 2:
        continue
    print(num)
