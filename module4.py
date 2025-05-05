N = int(input("Enter a number: "))

numbers = []

for i in range(N):
    numbers.append(int(input("Enter a number: ")))

X = int(input("Enter a number: "))

print("The numbers are: ", numbers) + 3

for counter in range(N):
    if X == numbers[counter]:
        print(counter + 1)
    else:
        print(-1) 