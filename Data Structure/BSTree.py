import argparse

class Node():
    #########################
    # DO NOT MODIFY CODES HERE
    #########################
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return str(self.value)


class BS_tree():
    def __init__(self):
        self.root = None

    def insert(self, key):          # insert one node
        if self.root:
            self._insert(key, self.root)
        else:
            self.root = Node(key)
    def _insert(self, key, curNode):  # recursively insert node
        if key < curNode.value:
            if curNode.left_child:
                self._insert(key, curNode.left_child)
            else:
                curNode.left_child = Node(key)
                curNode.left_child.parent = curNode
        elif key > curNode.value:
            if curNode.right_child:
                self._insert(key, curNode.right_child)
            else:
                curNode.right_child = Node(key)
                curNode.right_child.parent = curNode
        else:
            print("No way!!! There is the same value in this tree.")


    def inorder(self, output):      # print the in-order traversal of binary search tree
        # TODO
        self.inordertreelist = []
        if self.root is not None:
            self._inorderlist(self.root)
            self.inordertreelist = " ".join(str(i) for i in self.inordertreelist)
            return print(self.inordertreelist, file=output)
        else:
            return
    def _inorderlist(self,curnode):
        if curnode!=None:
            self._inorderlist(curnode.left_child)
            self.inordertreelist.append(curnode.value)
            self._inorderlist(curnode.right_child)

    def preorder(self, output):     # print the pre-order traversal of binary search tree
        # TODO
        self.preordertreelist = []
        if self.root is not None:
            self._preorderlist(self.root)
            self.preordertreelist = " ".join(str(i) for i in self.preordertreelist)
            return print(self.preordertreelist, file=output)
        else:
            return
    def _preorderlist(self,curnode):
        if curnode!=None:
            self.preordertreelist.append(curnode.value)
            self._preorderlist(curnode.left_child)
            self._preorderlist(curnode.right_child)

    def postorder(self, output):    # print the post-order traversal of binary search tree
        # TODO
        self.postordertreelist = []
        if self.root is not None:
            self._postorderlist(self.root)
            self.postordertreelist = " ".join(str(i) for i in self.postordertreelist)
            return print(self.postordertreelist, file=output)
        else:
            return
    def _postorderlist(self,curnode):
        if curnode!=None:
            self._postorderlist(curnode.left_child)
            self._postorderlist(curnode.right_child)
            self.postordertreelist.append(curnode.value)


    def find_max(self, output):     # print the maximum number in binary search tree
        # TODO
        current = self.root
        while current.right_child is not None:
            current = current.right_child
        return print(current.value, file=output)
    def find_min(self, output):     # print the minimum number in binary search tree
        # TODO
        current = self.root
        while current.left_child is not None:
            current = current.left_child
        return print(current.value, file=output)


    def delete(self, key):          # delete one node
        # TODO
        self.root = self._delete_node(self.root, key)
    def _delete_node(self, node, key):
        def minValueNode(node):
            current = node
            while(current.left_child):
                current = current.left_child
            return current
        if node is None:
            return node
        # different cases
        if key < node.value:
            node.left_child = self._delete_node(node.left_child,key)
        elif (key > node.value):
            node.right_child = self._delete_node(node.right_child,key)
        # key == node.value
        else:
            if node.left_child is None:
                temp = node.right_child
                node = None
                return temp
            elif node.right_child is None:
                temp = node.left_child
                node = None
                return temp
            temp =  minValueNode(node.right_child)
            node.value = temp.value
            node.right_child = self._delete_node(node.right_child, temp.value)
        return node


    def level(self, output):        # print the height of binary search tree(leaf = 0)
        # TODO
        if self.root != None:
            return print(self._height(self.root,0)-1, file=output)
        else:
            return
    def _height(self, curnode, cur_height):
        if curnode == None:
            return cur_height
        else:
            left_height = self._height(curnode.left_child,cur_height+1)
            right_height = self._height(curnode.right_child,cur_height+1)
            return max(left_height, right_height)


    # print the internal node in binary search tree from the smallest to the largest
    def internalnode(self, output):
        # TODO
        self.internallist = []
        if self.root != None:
            self.internallist = sorted(self._internal(self.root))
            self.internallist = " ".join(str(i) for i in self.internallist)
            return print(self.internallist, file=output)
        else:
            return
    def _internal(self, curnode):
        q = []
        q.append(curnode)
        while(len(q)): # when is not zero. that is, a new curnode
            curr = q[0]
            q.pop(0)
            isInternal = 0  
            if (curr.left_child):
                isInternal = 1
                q.append(curr.left_child)
            if (curr.right_child):
                isInternal = 1
                q.append(curr.right_child)
            if (isInternal):
                self.internallist.append(curr.value)
        return self.internallist


    def leafnode(self, output):     # print the leafnode in BST from left to right
        # TODO
        self.leaflist = []
        if self.root != None:
            self.leaflist = sorted(self._leaf(self.root))
            self.leaflist = " ".join(str(i) for i in self.leaflist)
            return print(self.leaflist, file=output)
        else:
            return
    def _leaf(self, curnode):
        # If node is leaf node,append its data
        if (not curnode.left_child and not curnode.right_child):
            self.leaflist.append(curnode.value)

        # If left child exists, check for leaf recursively
        if curnode.left_child:
            self._leaf(curnode.left_child)

        # If right child exists, check for leaf recursively
        if curnode.right_child:
            self._leaf(curnode.right_child)
        return self.leaflist


    def showtree(self, curNode):
        self.treelist.append(curNode.value)


    def main(self, input_path, output_path):
        #########################
        # DO NOT MODIFY CODES HERE
        #########################
        output = open(output_path, 'w')
        with open(input_path, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("insert"):
                    value_list = lines.split(' ')
                    for value in value_list[1:]:
                        self.insert(int(value))
                if lines.startswith('inorder'):
                    self.inorder(output)
                if lines.startswith('preorder'):
                    self.preorder(output)
                if lines.startswith('postorder'):
                    self.postorder(output)
                if lines.startswith('max'):
                    self.find_max(output)
                if lines.startswith('min'):
                    self.find_min(output)
                if lines.startswith('delete'):
                    value_list = lines.split(' ')
                    self.delete(int(value_list[1]))
                if lines.startswith('level'):
                    self.level(output)
                if lines.startswith('internalnode'):
                    self.internalnode(output)
                if lines.startswith('leafnode'):
                    self.leafnode(output)
        output.close()


if __name__ == '__main__':
    #########################
    # DO NOT MODIFY CODES HERE
    #########################
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str,
                        default='./input_3.txt', help="Input file root.")
    parser.add_argument("--output", type=str,
                        default='./output_3.txt', help="Output file root.")
    args = parser.parse_args()

    BS = BS_tree()
    BS.main(args.input, args.output)

