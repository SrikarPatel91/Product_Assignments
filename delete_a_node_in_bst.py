class Solution:
    def deleteNode(self, root, val):
        if root == None:
            return None

        if val < root.val:
            root.left = self.deleteNode(root.left, val)

        elif val > root.val:
            root.right = self.deleteNode(root.right, val)

        else:
            if root.left == None:
                return root.right

            if root.right == None:
                return root.left

            temp = root.right

            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root
