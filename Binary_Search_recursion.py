def binarySearch(arr,target,start,end):
        if (start <= end):
                mid = start + ((end - start)//2)
                if (target < arr[mid]):
                        return binarySearch(arr,target,start,mid - 1)
                elif (target > arr[mid]):
                        return binarySearch(arr,target,mid + 1,end)
                else :
                        return mid
        else:
                return -1

arr=[1,2,3,6,8,9,10]
target = int (input("Enter thr target valueyou want to search from array: "))
print("Position of target is : ")
print(binarySearch(arr,target,0,len(arr)-1))

                        
        