class Node(object):

    def __init__(self, value=None):
        self.children = {}
        self.value = value
        self.word = None


class Trie(object):

    def __init__(self):
        self.node = Node()

    def append(self, item):
        cur_node = self.node
        for i in item:
            if i in cur_node.children:
                cur_node = cur_node.children[i]
            else:
                new_node = Node(i)
                cur_node.children[i] = new_node
                cur_node = new_node
        cur_node.word = item
