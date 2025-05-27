def bin_search(arr, item): # Take input: arr (sorted list) and item (element to find)
    low = 0  # Start index (leftmost element)
    high = len(arr) - 1  # End index (rightmost element)

    while low <= high: # Continue searching while the range is valid (low is before or equal to high)
        mid = (low + high) // 2  # Find middle index
        guess = arr[mid]  # Get the middle element

        if guess == item:  # Element found
            return mid  # Return index of found element
        elif guess > item:  # If middle element is greater, search left half
            high = mid - 1  # Ignore elements **after** mid (reduce search space)
        else:  # If middle element is smaller, search right half
            low = mid + 1  # Ignore elements **before** mid
    return None  # If not found, return None

def insert_sort(arr):  
    for i in range(1, len(arr)):  # Start sorting from the 2nd element (index 1)
        key = arr[i]  # The element to be inserted at the correct position
        j = i - 1  # Pointer to compare with previous elements

        while j >= 0 and arr[j] > key:  # Shift elements **greater** than key to the right
            arr[j+1] = arr[j]  # Move current element one step right
            j -= 1  # Move pointer one step left

        arr[j+1] = key  # Place key in its correct sorted position
    return arr  # Return the sorted array


a1 = [int(input("enter the elements of the array>> ")) for _ in range(5)]
sorted_arr= insert_sort(a1)

item= int(input("enter the element to find>> "))

get_item= bin_search(sorted_arr, item)
print(" your sorted array >> ",sorted_arr)
print(" your item >>", get_item)






                