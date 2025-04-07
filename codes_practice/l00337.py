# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def travel(r: TreeNode):
            if not r.left and not r.right:
                return r.val, 0
            sub1 = 0
            sub2 = 0
            if r.left:
                ret1, ret2 = travel(r.left)
                sub1 += ret1
                sub2 += ret2
            if r.right:
                ret1, ret2 = travel(r.right)
                sub1 += ret1
                sub2 += ret2
            cur = max(sub1, r.val+sub2)
            return cur, sub1

        return travel(root)[0]


s = Solution()

n = TreeNode(3,
             TreeNode(4,
                      TreeNode(1), TreeNode(3)),
             TreeNode(5,
                      None, TreeNode(1))
             )

print(s.rob(n))
