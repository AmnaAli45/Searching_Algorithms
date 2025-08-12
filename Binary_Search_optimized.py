def Binary_Search(arr,target):
    start = 0
    end = len(arr) - 1
    
    while (start <= end) :
        mid = start + ((end - start)//2)
        if arr[mid] < target :
            start = mid + 1
        elif arr[mid] > target:
            end = mid -1
        else :
            return mid
        
    return -1

arr = [-1,0,3,4,5,9,12]
target = int (input("Enter thr target valueyou want to search from array: "))
print("Position of target is : ")
print (Binary_Search(arr,target))

