class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else: 
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
            
            

    
sol = Solution()
asteroids = [10,2,-5]
asteroids1 = [5,10,-5]
asteroids2 = [8,-8]
print(sol.asteroidCollision(asteroids=asteroids))
print(sol.asteroidCollision(asteroids=asteroids1))
print(sol.asteroidCollision(asteroids=asteroids2))