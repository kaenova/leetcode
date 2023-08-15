class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        finalList = [[1]]
        if rowIndex == 0:
            return finalList[0]
        
        finalList.append([1,1])
        if rowIndex == 1:
            return finalList[1]
        
        for i in range(1, rowIndex):
            listAbove = finalList[i]
            currentList = []
            
            currentList.append(1)
            for i in range(1, len(listAbove)):
                currentList.append(listAbove[i] + listAbove[i-1])
            currentList.append(1)
            
            finalList.append(currentList)
        
        return finalList[rowIndex]