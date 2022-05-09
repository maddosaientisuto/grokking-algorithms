import sys


def findSmallest(arr):

    smallest = arr[0]  # stores the smallest value
    smallest_index = 0  # stores the index of smallest value

    for i in range(1, len(arr)):

        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selectionSort(arr):
    # sorts an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == "__main__":
    print(selectionSort([5, 3, 6, 2]))
