# O(n)
class Solution:
    
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        steps = [0 for _ in range(n)]
        steps[0] = 1
        steps[1] = 2
        
        for i in range(2, n):
            steps[i] = steps[i-1] + steps[i-2]
        
        return steps[-1]
        


"""
Brute Force w/o memo
2
1 1

3
1 1 1
2 1
1 2

4
1 1 1 1
2 1 1 => 2 2
1 2 1 
1 1 2 => 2 2

5
1 1 1 1 1
2 1 1 1 => 2 2 1 => []
1 2 1 1 => 1 2 2 => []
1 1 2 1 => 
1 1 1 2


# O(n^n-1)
class Solution:
    def encodeListStr(self, ls):
        return str(ls)

    def merge(self, arr):
        # Dont return anything if there's no array
        if len(arr) == 0:
            return 
        
        # Return something inside that array
        if len(arr) == 1:
            return self.encodeListStr(arr)
        
        # Create new list of builded 2
        build_arr = []
        for idx in range(1, len(arr)):
            can_be_merge = arr[idx] == 1 and arr[idx - 1] == 1
            if can_be_merge:
                build_arr.append(arr[:(idx - 1)] + [2] + arr[idx+1:])
        
        # Prepare final array
        final_arr = []

        # Encode build arr
        encode_build_arr = [self.encodeListStr(x) for x in build_arr]
        final_arr += encode_build_arr

        # Inside build array, do recursively
        for x in build_arr:
            final_arr += self.merge(x) 

        # Dont return anything if it's on empty
        if len(final_arr) == 0:
            return []
        
        # Return list of any able combination
        return final_arr
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        final_arr = []
        ones = [1 for _ in range(n)]
        final_arr = [self.encodeListStr(ones)] + self.merge(ones)
        final_arr = set(final_arr)
        return len(final_arr)

"""

        