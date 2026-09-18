class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0: #we plant the one and check
                return 1 >= n
            
        placed = 0
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                placed+=1
            elif i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                placed+=1
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                placed+=1
            else:
                pass
        return placed >= n



                