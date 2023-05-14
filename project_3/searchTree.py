class SearchTree:
    
    # Depth-first search algorithm
    def dfs(self, start_node, goal_node, search_tree):
        """
        Depth-first search algorithm.
        
        Args:
            start_node (any): The start node.
            goal_node (any): The goal node.
            search_tree (dict): A dictionary representing the search tree. The keys are the nodes in the tree,
                                 and the values are lists of tuples representing the children of the node and their
                                 associated edge costs.
        
        Returns:
            float: The cost to reach the goal node from the start node.
        """
        visited = set() # Set to keep track of visited nodes
        stack = [(start_node, 0)] # Stack to keep track of nodes to explore, initially contains the start node and its cost
        while stack:
            node, cost = stack.pop() # Pop a node and its cost from the stack
            if node == goal_node: # If the node is the goal node, return its cost
                return cost
            if node not in visited: # If the node has not been visited before
                visited.add(node) # Add it to the set of visited nodes
                for child, edge_cost in reversed(search_tree.get(node, [])): # For each child of the node in reverse order
                    stack.append((child, cost + edge_cost)) # Add the child and its cost to the stack
        return float('inf') # If the goal node is not found, return infinity
    
    # Breadth-first search algorithm
    def bfs(self, start_node, goal_node, search_tree):
        """
        Breadth-first search algorithm.
        
        Args:
            start_node (any): The start node.
            goal_node (any): The goal node.
            search_tree (dict): A dictionary representing the search tree. The keys are the nodes in the tree,
                                 and the values are lists of tuples representing the children of the node and their
                                 associated edge costs.
        
        Returns:
            float: The cost to reach the goal node from the start node.
        """
        visited = set() # Set to keep track of visited nodes
        queue = [(start_node, 0)] # Queue to keep track of nodes to explore, initially contains the start node and its cost
        while queue:
            node, cost = queue.pop(0) # Pop a node and its cost from the queue
            if node == goal_node: # If the node is the goal node, return its cost
                return cost
            if node not in visited: # If the node has not been visited before
                visited.add(node) # Add it to the set of visited nodes
                for child, edge_cost in search_tree.get(node, []): # For each child of the node
                    queue.append((child, cost + edge_cost)) # Add the child and its cost to the queue
        return float('inf') # If the goal node is not found, return infinity
   
    def h(self, node, goal_node, search_tree):
        """
        Heuristic function for A* algorithm.
        
        Args:
            node (any): The current node.
            goal_node (any): The goal node.
            search_tree (dict): A dictionary representing the search tree. The keys are the nodes in the tree,
                                and the values are lists of tuples representing the node's children and their edge costs.
        
        Returns:
            The heuristic value of the node.
        """
        if node == goal_node: # If the node is the goal node, return 0
            return 0
        elif not search_tree.get(node): # If the node has no children, return infinity
            return float('inf')
        else: # If the node has children
            # Return the minimum edge cost plus the heuristic value of the child node recursively
            return min(edge_cost + self.h(child, goal_node, search_tree) for child, edge_cost in search_tree[node])
        
    # Hill-climbing algorithm with A* heuristic
    def hill_climbing(self, start_node, goal_node, search_tree):
        """
        Implements the hill-climbing algorithm with A* heuristic to find the path from start_node to goal_node in a search tree.

        Args:
            start_node (any): The start node.
            goal_node (any): The goal node.
            search_tree (dict): A dictionary representing the search tree. The keys are the nodes in the tree,
                                and the values are lists of tuples representing the node's children and their edge costs.

        Returns:
            The cost of the path from start_node to goal_node if found, otherwise returns infinity.
        """
        # Set the current node to the start node and initialize the cost to 0
        node = start_node
        cost = 0
        # Continue until the current node is the goal node
        while node != goal_node:
            # Get the children of the current node from the search tree
            children = search_tree.get(node, [])
            # If the current node has no children, return infinity
            if not children:
                return float('inf')
            # Calculate the heuristic values of each child and select the one with the minimum heuristic value
            h_values = [(edge_cost + self.h(child, goal_node, search_tree), child, edge_cost) for child, edge_cost in children]
            min_h, min_child, min_edge_cost = min(h_values)
            # If the minimum heuristic value is not better than the current node's heuristic value, return infinity
            if min_h >= min_edge_cost + self.h(node, goal_node, search_tree):
                return float('inf')
            # Set the current node to the selected child and add its edge cost to the total cost
            node = min_child
            cost += min_edge_cost
        # Return the cost of the path from start_node to goal_node
        return cost    
        
    def main(self):
        search_tree = {
            'S': [('A', 3), ('D', 4)],
            'A': [('B', 4), ('D', 5)],
            'B': [('C', 4), ('E', 5)],
            'D': [('E', 2)],
            'E': [('F', 4)],
            'F': [('G', 3)]
        }
        
        start_node = 'S'
        goal_node = 'G'
        dfs_result = self.dfs(start_node, goal_node, search_tree)
        print("DFS result:", dfs_result)
        
        bfs_result = self.bfs(start_node, goal_node, search_tree)
        print("BFS result:", bfs_result)
        
        hill_climbing_result = self.hill_climbing(start_node, goal_node, search_tree)
        print("Hill climbing result:", hill_climbing_result)

if __name__ == '__main__':
    search_tree = SearchTree()
    search_tree.main()