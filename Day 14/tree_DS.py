from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def bfs(self):
        if not self.root:
            return []

        queue = deque([self.root])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def search(self, value):
        if not self.root:
            return False

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.value == value:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False

    # Phương thức in cấu trúc cây (đơn giản) để dễ hình dung
    def print_tree(self, node, level=0):
        if node:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)

# Tạo một cây mẫu
tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Duyệt và in kết quả BFS
print("Duyệt theo chiều ngang (BFS):", tree.bfs())

# Tìm kiếm một giá trị
value_to_search = 3
if tree.search(value_to_search):
    print(f"Tìm thấy giá trị {value_to_search} trong cây.")
else:
    print(f"Không tìm thấy giá trị {value_to_search} trong cây.")

# In cấu trúc cây
print("\nCấu trúc cây:")
tree.print_tree(tree.root)
