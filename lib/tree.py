class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        def dfs(node):
            if not node:
                return None
            
            # Check if the current node matches the ID
            if node.get('id') == id:
                return node
            
            # Recursively search through children
            for child in node.get('children', []):
                result = dfs(child)
                if result:
                    return result
            
            return None
        
        return dfs(self.root)
