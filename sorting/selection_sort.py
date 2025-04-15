from typing import List

def selection_sort(A: List[int]) -> List[int]:
    """
        Selection Sort
        Takes in an array of numbers (n)
        Sorts the list by repeatedly selecting
        the smallest remaining element and moving
        it to its correct position.
    """

    for i in list(range(len(A))):
        minvalue = A[i]
        minindex = i
        
        for j in list(range(i, len(A))):
            if A[j] < minvalue:
                minvalue = A[j]
                minindex = j

        A[i], A[minindex] = A[minindex], A[i]

    return A

test_list = [1,5,4,7,5,8,2]
print(selection_sort(test_list))
