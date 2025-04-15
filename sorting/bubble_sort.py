from typing import List

def bubble_sort(A: List[int]) -> List[int]:
    """
        BUBBLE SORT
        Takes an array of numbers (n)
        Sorts the list by bubbling up the smallest element
        through a series of swaps until it reaches its
        proper position in the array
    """
    for i in list(range(len(A))):
        for red in list(range(len(A)-1, i, -1)):
            if A[red-1] > A[red]:
                A[red-1], A[red] = A[red], A[red-1]

    return A

test_array = [10,9,2,1,3,4,5,7,6,8]
print(test_array)
print(bubble_sort(test_array))
