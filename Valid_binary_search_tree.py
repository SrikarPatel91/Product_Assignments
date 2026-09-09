class Solution:
    def isValidBST(self, root):
            def find(self, root, min, max):
                if root == None:
                    return True

                if root.val <= min or root.val >= max:
                    return False

            return self.find(root.left, min, root.val) and self.find(root.right, root.val, max)
        return self.find(root, float('-inf'), float('inf'))
