class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output=[]
        num = 1
        while(len(target) != 0):
            if target[0] == num:
                output.append("Push")
                target.pop(0)
            else:
                output.append("Push")
                output.append("Pop")
            num+=1
                
        return output