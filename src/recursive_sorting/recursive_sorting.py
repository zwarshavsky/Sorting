
arr = [38,27,43,3,9,82,65,67]


# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge(arrA, arrB):
    # elements = len( arrA ) + len( arrB )
    if len(arrA) == 1:
        if arrA[0] > arrB[0]:
            arrA[0],arrB[0] = arrB[0],arrA[0]
            l = [arrA[0],arrB[0]]
        else:
            l = [arrA[0],arrB[0]]
    else:
        l = arrA + arrB
        for i in range(0, len(l) - 1):
            cur_index = i
            smallest_index = cur_index
            for j in range(cur_index, len(l)):
                if l[smallest_index] > l[j]:
                    l[smallest_index],l[j] = l[j],l[smallest_index]

    return l


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) == 1:
        print("base case reached:",arr)
        return arr
    else:
        print("recursive case started:",arr)
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        print("recursive case reached:",left,right)
        return (merge(left,right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

if __name__ == "__main__":
    print(merge_sort(arr))
