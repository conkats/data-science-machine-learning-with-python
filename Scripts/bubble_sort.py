#Explanation of the Sorting Algorithm (Bubble Sort)
#One of the simplest sorting algorithms is Bubble Sort. The logic behind Bubble Sort is to repeatedly step through the list, compare adjacent elements, and swap them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
#
#Steps of the Bubble Sort Algorithm:
#1.Start at the beginning of the list.
#2.Compare the first two elements:
#3.If the first element is larger than the second, swap them.
#If not, leave them as is.
#4.Move to the next pair of adjacent elements and repeat the comparison and swap process.
#Continue this until you reach the end of the list. At this point, the largest element will have "bubbled" to the end.
#5.Repeat the process for the rest of the list, excluding the last element (since it's already sorted).
#6.Continue until no more swaps are needed.#
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Set a flag to check if any swap happened in tshis pass
        swapped = False
        # Last i elements are already in place, no need to compare them
        # Inner loop (for j in range(0, n-i-1)): This loop compares adjacent elements and swaps them if needed. The n-i-1 ensures that you do not recheck the sorted portion of the list.
        for j in range(0, n-i-1):
            # Compare the adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
