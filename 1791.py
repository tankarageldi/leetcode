class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        dict = {}
        for edge in edges:
            for item in edge:
                if item in dict:
                    dict[item] += 1
                else:
                    dict[item] = 1
        for key in dict:
            if dict[key] == len(edges):
                return key