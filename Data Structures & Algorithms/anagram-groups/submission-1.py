class Solution:

    def getKey(self, s:str):
        return "".join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}
        output = []

        for i,s in enumerate(strs):
            key = self.getKey(s)
            indices = hashMap.get(key, [])
            indices.append(s)
            hashMap[key] = indices
        
        for collection in hashMap.values():
            output.append(collection)

        return output