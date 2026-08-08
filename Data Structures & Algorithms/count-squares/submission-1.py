class CountSquares:

    def __init__(self):
        self.pFrqMap = {}

    def add(self, point: List[int]) -> None:
        key = tuple(point)
        self.pFrqMap[key] = self.pFrqMap.get(key, 0) + 1
        

    def count(self, point: List[int]) -> int:
        #strategy one: 

        qX = point[0] # querry X
        qY = point[1] # querry Y
        #figure out unique distance of all points
        #then check if squares of that disitance exist
        #only record distance where either gx,gy is same
        res = 0
        possibleSides = set()

        for existPoint in self.pFrqMap:
            gX = existPoint[0] # graph x
            gY = existPoint[1] # graph y
            if gX == qX and gY != qY:
                # print("added side from X same",(qX,qY),(gX,gY))
                possibleSides.add(abs(gY-qY))
            elif gY == qY and gX != qX:
                # print("added side from y SAME",(qX,qY),(gX,gY))
                possibleSides.add(abs(gX-qX))
        
        # print(possibleSides)

        for side in possibleSides:
            #now check if sqaure existing in quadrants 1-4 relative to querry for each dist 
            
            #quad1 (top right sqaure)
            p1,p2,p3 = (qX+side,qY), (qX + side,qY + side), (qX,qY + side)

            if p1 in self.pFrqMap and p2 in self.pFrqMap and p3 in self.pFrqMap:
                res+= self.pFrqMap[p1] * self.pFrqMap[p2] * self.pFrqMap[p3]

            #quad2 (top left square)
            p1,p2,p3 = (qX-side,qY), (qX - side,qY + side), (qX,qY + side)

            if p1 in self.pFrqMap and p2 in self.pFrqMap and p3 in self.pFrqMap:
                res+= self.pFrqMap[p1] * self.pFrqMap[p2] * self.pFrqMap[p3]

            #quad3 (bottom left sq)
            p1,p2,p3 = (qX-side,qY), (qX - side,qY - side), (qX,qY - side)

            if p1 in self.pFrqMap and p2 in self.pFrqMap and p3 in self.pFrqMap:
                res+= self.pFrqMap[p1] * self.pFrqMap[p2] * self.pFrqMap[p3]

            #quad4 (bottom right sq)
            p1,p2,p3 = (qX+side,qY), (qX + side,qY - side), (qX,qY - side)
            
            if p1 in self.pFrqMap and p2 in self.pFrqMap and p3 in self.pFrqMap:
                res+= self.pFrqMap[p1] * self.pFrqMap[p2] * self.pFrqMap[p3]

        return res








