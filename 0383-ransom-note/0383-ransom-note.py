class Solution:
    def dictionaryAddCounter(self, dictionary: Dict[str, int], key: str) -> Dict[str, int]:
        if key not in dictionary:
            dictionary[key] = 1
        else:
            dictionary[key] += 1
        
        return dictionary
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteLength = len(ransomNote)
        magazineLength = len(magazine)
        counter = 0
        
        # Building dictionary
        rDict = {}
        mDict = {}
        while counter < ransomNoteLength or counter < magazineLength:
            if counter < ransomNoteLength:
                rDict = self.dictionaryAddCounter(rDict, ransomNote[counter])
            
            if counter < magazineLength:
                mDict = self.dictionaryAddCounter(mDict, magazine[counter])
            
            counter += 1
            
        for key in rDict:
            if key not in mDict:
                return False
            
            if rDict[key] > mDict[key]:
                return False
            
        return True