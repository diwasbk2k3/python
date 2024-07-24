#linear search
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter the target: "))

for i in range(len(a)):
    if a[i] == target:
        print("Target found at", i, "index")
        break
else:
    print("Target not found")
