
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        from_left = False
        if root:
            ret = []
            curr = [root]
            while curr:
                ret.append([x.val for x in curr])
                new_arr=[]
                for i in range(len(curr)-1, -1, -1):
                    if from_left:
                        if curr[i].left:
                            new_arr.append(curr[i].left)
                        if curr[i].right:
                            new_arr.append(curr[i].right)
                    else:
                        if curr[i].right:
                            new_arr.append(curr[i].right)
                        if curr[i].left:
                            new_arr.append(curr[i].left)
                from_left = not from_left
                curr = new_arr
            return ret
                        
        else:
            return []
        


def main():
    a = TreeNode(3,
                 left= TreeNode(9),
                 right= TreeNode(20,
                                 left=TreeNode(15),
                                 right=TreeNode(7)
                                 ) 
                 )
    
    s = Solution()
    print(s.zigzagLevelOrder(a))


if __name__=='__main__':
    main()
     