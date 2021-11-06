# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        #왼쪽 다 돌기
        if root.left:
            self.minDiffInBST(root.left)
        
        #나오면서 계산값 비교해서 result 값 수정
        self.result = min(self.result, root.val - self.prev)
        #지금 값을 탈출 전에 이전값으로 설정
        self.prev = root.val
        
        #오른쪽 다 돌기
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result