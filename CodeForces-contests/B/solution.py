def count_distinct_values(lst, k):
    modified_list = set(ai % k for ai in lst)
    return len(modified_list)

def find_k(lst):
    low, high = 1, 10**18

    while low < high:
        mid = (low + high) // 2
        distinct_values = count_distinct_values(lst, mid)

        if distinct_values == 2:
            return mid
        elif distinct_values < 2:
            high = mid
        else:
            low = mid + 1

    return None

# Example usage
input_list = [8, 15, 22, 30 ]
result_k = find_k(input_list)

print(f"The value of k for the given list is: {result_k}")
