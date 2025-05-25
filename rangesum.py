def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

def range_sum(prefix, L, R):
    return prefix[R] - (prefix[L - 1] if L > 0 else 0)

def main():
    # Take array input
    arr = list(map(int, input("Enter array elements (space separated): ").split()))
    prefix = prefix_sum(arr)

    # Take range query
    L, R = map(int, input("Enter L and R (0-based): ").split())
    print("Range Sum:", range_sum(prefix, L, R))

main()
