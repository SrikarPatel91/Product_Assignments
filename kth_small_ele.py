class Solution:
    def kthSmallest(self, root, k):
         res = []
         def inorder(self, root, list):
            if root:
                inorder(root.left, list)
                list.append(root.val)
                inorder(root.right, list)
        inorder(root, list)
        return list[k - 1]
