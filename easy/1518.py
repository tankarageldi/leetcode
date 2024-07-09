class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinked_bottles = 0

        while numBottles >= numExchange:
            drinked_bottles += numExchange
            numBottles -= numExchange
            numBottles += 1
        return drinked_bottles + numBottles
             