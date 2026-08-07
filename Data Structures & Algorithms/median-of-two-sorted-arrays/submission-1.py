class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if len(B) < len(A): #swap so A is smaller
            A,B=B,A
        total = len(A) + len(B)
        half = total//2

        l,r = 0,len(A)-1
        while True:
            midIndexA = (l+r)//2
            partIndexB =  half - (midIndexA+1) -1 # need -1 as zero indexed

            APartValue = A[midIndexA] if midIndexA >= 0 else -float('inf')
            APartRight = A[midIndexA+1] if midIndexA+1 < len(A) else float('inf')
            
            BPartValue = B[partIndexB] if partIndexB >= 0 else -float('inf')
            BPartRight = B[partIndexB+1] if partIndexB+1 < len(B) else float('inf')
            
            #correct partion values found
            if APartValue <= BPartRight and BPartValue <= APartRight: 
                if total % 2 == 1:
                    return min(APartRight,BPartRight)
                else:
                    return (max(BPartValue,APartValue) + min(APartRight,BPartRight)) / 2
            
            elif APartValue > BPartRight: #so our partian value is too big move right down
                r = midIndexA-1
            else: #partion value too big move left up
                l = midIndexA+1





        
        #
        
        
        
        # brute force
        # # Lets first merge and then just find middle
        # l1 = 0
        # l2 = 0
        # merged_arr = [0] * (len(nums1)+len(nums2))
        # i = 0
        # while l1 < len(nums1) and l2 < len(nums2):
        #     if nums1[l1] < nums2[l2]:
        #         merged_arr[i] = nums1[l1]
        #         l1+=1
        #     else:
        #         merged_arr[i] = nums2[l2]
        #         l2+=1
        #     i+=1
        
        # while l1 < len(nums1):
        #     merged_arr[i] = nums1[l1]
        #     l1+=1
        #     i+=1
        # while l2 < len(nums2):
        #     # print(merged_arr,i,l1,l2)
        #     merged_arr[i] = nums2[l2]
        #     l2+=1
        #     i+=1
        
        # l_fin = 0
        # r_fin = len(merged_arr)
        # mid = (l_fin+r_fin)//2
        # if len(merged_arr)%2==0:
        #     return (merged_arr[mid]+merged_arr[mid-1])/2.0
        # else:
        #     return merged_arr[mid]

        # #great can i do a faster merge? this is O(n) currently
        # # IDEA do arrays follow this structure:
        # # x1 x2 ... x(n/2) ... MEDIAN1 x(n/2+1) ... x(n) | y1 y2 ... y(n/2) MEDIAN2 y(n/2+1) ... y(n)
        # # ignoring off by one bs, MUST the median exist between MEDIAN1 and MEDIAN2 or MEDIAN2 and MEDIAN1?
        # # say x = [1,2,3], y = [7,23,34]....yes??
        
                
        