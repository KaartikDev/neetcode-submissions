class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        balls = 0
        moves = 0
        for i in range(len(boxes)):
            res[i] += moves
            
            balls += int(boxes[i])
            moves += balls
        
        balls = 0
        moves = 0
        # print("hi")
        for i in range(len(boxes)-1,-1,-1):
            res[i] += moves
            # print(moves)
            balls += int(boxes[i])
            moves += balls

        return res