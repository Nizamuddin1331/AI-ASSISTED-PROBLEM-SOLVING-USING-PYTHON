def find_common(a, b):
    res = []
    for i in a:
        for j in b:
            if i == j:
                res.append(i)
    return res

# Taking input from the user
list1 = list(map(int, input("Enter elements of List 1 separated by space: ").split()))
list2 = list(map(int, input("Enter elements of List 2 separated by space: ").split()))

# Calling the function
result = find_common(list1, list2)

# Output
print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", result)
