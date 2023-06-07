class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash = {}
        for i in range(len(arr)):
            temp = arr[i] * 2
            hash[temp] = i
        for i in range(len(arr)):
            if arr[i] in hash and hash[arr[i]] != i:
                return True  
        return False
