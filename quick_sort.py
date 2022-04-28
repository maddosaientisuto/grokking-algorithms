import sys


def quicksort(array):
    if len(array) < 2:
        return array  # Base case: arrays with zero and one element are already "sorted"
    else:
        pivot = array[0]  # Recursive case
        less = [
            i for i in array[1:] if i <= pivot
        ]  # sub-array of all elements less than the pivot
        greater = [
            i for i in array[1:] if i > pivot
        ]  # sub-array of all elements greater than pivot

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    print(quicksort([10, 5, 2, 3]))
