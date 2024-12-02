# Searching and Sort
import random #for testing
# Searching
# Linear
def linear(data, target):
    """
    Linear Search:
    Search one by one through data until target is found and then return index of the target.

    If target is not found, an index of -1 will be returned.
    """
    for i, item in enumerate(data):
                # returns a tuple
                # i - Index      item - the value
        if item==target:
            return i
    return -1
        
# Binary
def binary(data, target):
    """
    Binary Search:
    REQUIRES SORTED ARRAY/LIST
    Search through the array/list by going halfway through and determining if the target is less than or greater than the current value.

    If target is not found, an index of -1 will be returned.
    """

    halfway=len(data)//2
    #base case
    if data[halfway] == target:
        return halfway
    elif target < data[halfway]:
        result = binary(data[:halfway],target)
        if result!=-1:
            return (result)
    else:
        result = binary(data[halfway+1:],target)
        if result!=-1:
            return (halfway+1+result)
    # if no matches
    return -1

# Sorting
# Bubble Sort
def bubbleSort(data):
    """
    Bubble Sort:
    Goes from index 0 to last index, and "bubbles" the largest value to the top of the list/array until list is sorted. 
    """

# Merge Sort

def mergeSort(data):
    """
    Merge Sort:
    Splits list/array until single sized arrays, then sorts and merges the arrays into sorted list/array and returns sorted list/array.
    """
    if len(data)<=1:
        return data

    half1 = mergeSort(data[:len(data)//2]) 
    if half1 == None:
        return half1
    
    half2 = mergeSort(data[len(data)//2:])
    if half2 == None:
        return half2
    
    
    result = []
    while len(half1)>=1 and len(half2)>=1:
        #compare first values - then accordingly add the smaller value into the results list
        if half1[0]<half2[0]:
            result.append(half1.pop(0))
        else:
            result.append(half2.pop(0))
    # add the remaining last value in
    result+=half1+half2
    return result


#myList=[1,2,3,4,5,16]
#random.shuffle(myList)
#print("Unsorted List: ",myList)
#print(mergeSort(myList))