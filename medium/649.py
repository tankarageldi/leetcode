class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = []
        dir = []
        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                rad.append(i)
            else:
                dir.append(i)
        
        # while rad is not None and dir is not None:
        #     if rad[0] < dir[0]:
        #         rad.pop(n)
        #     else:
        #         dir.append(n)
            
        if rad is not None:
            return "Radiant"
        else:
            return "Dire"
        # not working