# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# git add . && git commit -m "completed serialize_and_deserialize_binary_tree" && git push && exit


# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "None"

        return (
            str(root.val)
            + " "
            + self.serialize(root.left)
            + " "
            + self.serialize(root.right)
        )

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = list(data.split(" "))

        def helper(data_list):
            head_data = data_list[0]
            if head_data == "None":
                return None, data_list[1:]

            head_node = TreeNode(data_list[0])

            if len(data_list) > 1:
                left_node, data_list = helper(data_list[1:])
                head_node.left = left_node

                if len(data_list) > 0:
                    right_node, data_list = helper(data_list)
                    head_node.right = right_node

                return head_node, data_list
            else:
                return head_node, data_list[1:]

        return helper(data_list)[0]
