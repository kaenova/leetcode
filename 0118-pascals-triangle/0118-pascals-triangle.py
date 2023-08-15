class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        finalList = [[1]]
        if numRows == 1:
            return finalList
        
        finalList.append([1,1])
        if numRows == 2:
            return finalList
        
        for i in range(1, numRows - 1):
            listAbove = finalList[i]
            currentList = []
            
            currentList.append(1)
            for i in range(1, len(listAbove)):
                currentList.append(listAbove[i] + listAbove[i-1])
            currentList.append(1)
            
            finalList.append(currentList)
        
        return finalList