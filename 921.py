class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        stack=[]
        
        for i in s:
            
            if i == '(':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    count+=1
                    
        count = count + len(stack)
        return count
 
