def find_in_range(arr, min_val, max_val):
    result = []
    for x in arr:
        if min_val <= x <= max_val:
            result.append(x)
    return result


ints = [1, 5, 8, 12, 3]
floats = [1.5, 3.2, 7.8, 2.1]
chars = ['a', 'd', 'h', 'c']

print(find_in_range(ints, 3, 10))
print(find_in_range(floats, 2.0, 5.0))
print(find_in_range(chars, 'b', 'f'))
