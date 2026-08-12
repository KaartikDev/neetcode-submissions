class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:


        #first do in place swpas shoving elements right via proceessing rows right to left
        STONE = "#"
        OBS = "*"
        AIR = "."
        for row in boxGrid:
            # i = len(row) - 2
            # while i > -1:
            #     if i <= len(boxGrid) - 2 and row[i] == STONE and row[i+1] == AIR:
            #         row[i] = AIR
            #         row[i+1] = STONE
            #         i+=1
            #     else:
            #         i-=1

            #reset write to left of any obstacle once encountered
            # or shift write left when rock falls to air spot
            write = len(row) - 1
            for i in range(len(row)-1,-1,-1):
                if row[i] == OBS:
                    write = i-1 # one to left could be valid
                elif row[i] == STONE:
                    row[i] = AIR
                    row[write] = STONE
                    write-=1
        
        # print(boxGrid)
        rotated = []
        
        for col in range(len(boxGrid[0])):
            newRow = []
            for row in range(len(boxGrid)):
                newRow.append(boxGrid[row][col])
            rotated.append(newRow[::-1]) #a rotation has rows reversed
        
        # print(rotated)
        return rotated
