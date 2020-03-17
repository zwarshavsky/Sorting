
l = [11, 35, 17, 15, 5]
print(l)

# TO-DO: Complete the selection_sort() function below 
def selection_sort(l=l):
    # loop through n-1 elements
    for i in range(0, len(l) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(l)):
            if l[smallest_index] > l[j]:
                l[smallest_index],l[j] = l[j],l[smallest_index]
    return l


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(l=l):
    swapped = True
    while swapped == True:
        swapped = False 
        for index in range(len(l)-1):
            # print(index)
            if l[index] > l[index+1]:
                # print("before:",l[index],l[index+1])
                l[index],l[index+1] = l[index+1],l[index] 
                swapped = True
            #     print("after:",l[index],l[index+1])
            #     print("bigger:",index)
            # else:
            #     print("smaller:",index)
    return l 


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

if __name__ == "__main__":

    print(selection_sort())
    print(bubble_sort())