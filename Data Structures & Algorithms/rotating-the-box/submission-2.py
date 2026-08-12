class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        #do gravity in place, assume gravity points to the right
        STONE = "#"
        OBS = "*"
        AIR = "."
        for row in boxGrid:
            #reset write to the LEFT of any obstacle once encountered
            #OR shift write left when rock falls to air spot
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
