class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        #lets implement merge sort


        def merge(arr1,arr2):
            res = []
            i,j = 0,0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    res.append(arr1[i])
                    i+=1
                else:
                    res.append(arr2[j])
                    j+=1
            
            while i < len(arr1):
                res.append(arr1[i])
                i+=1
            while j < len(arr2):
                res.append(arr2[j])
                j+=1
            
            return res
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            l = 0
            r = len(arr)
            m = (r+l)//2
            leftSorted = mergeSort(arr[:m])
            rightSorted = mergeSort(arr[m:])
            return merge(leftSorted,rightSorted)
        
        return mergeSort(nums)







