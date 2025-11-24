def reverse_slicing(lst):
    return lst[::-1]

def reverse_loop(lst):
    result = []
    for item in lst:
        result.insert(0, item)
    return result

def reverse_builtin(lst):
    temp = lst.copy()
    temp.reverse()
    return temp

if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5]
    print("Original:", sample)
    print("Slicing:", reverse_slicing(sample))
    print("Loop:", reverse_loop(sample))
    print("Built-in:", reverse_builtin(sample))
