class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        ans = [0] * len(boxes)

        for i in range(len(boxes)):
        # iterate through all boxes 
            if boxes[i] == "1": # if box has a ball, we need to calculate the number of moves to move this ball to the other boxes
                for j in range(len(boxes)):
                    ans[j] += abs(j-i) # calculates the moves of the ball from ith box to the rest of the boxes.
                
        return ans
                
        