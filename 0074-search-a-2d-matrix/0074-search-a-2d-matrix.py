class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Because of ascending orders, we can utilize to check if target in which row
        pivot_idx = 0
        for i in range(len(matrix)):
            pivot_elm = matrix[i][0]
            if pivot_elm == target:
                return True
            if pivot_elm > target:
                pivot_idx = i - 1
                break
            pivot_idx = i
        
        row_elms = matrix[pivot_idx]
        print(row_elms)
        for elm in row_elms:
            if elm == target:
                return True

        return False