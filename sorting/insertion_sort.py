
def insertion_sort(A: list[int]) -> list[int]:
    """
    Sorts a list by building a sorted portion 
    one element at a time, inserting each new 
    element into its correct position.
    """
    for i in list(range(len(A))):
        temp = A[i]

        red = i - 1

        while red >= 0 and A[red] > temp:
            A[red+1] = A[red]
            red -= 1

        A[red+1] = temp

    return A


test_list = [1,5,4,7,5,8,2]
print(insertion_sort(test_list))
