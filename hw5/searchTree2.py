'''

a) To implement the search tree in Python, we can use a class to represent
each node in the tree. Each node will have a state (the current
configuration of the puzzle), a parent node (the node that led to this
state), and a list of child nodes (the possible states that can be reached
from this state). We can also define methods for generating the child
nodes, checking if a state is the goal state, and printing the path from
the start state to the current state.

b) Code below

c) Heurisitc hill_climbing search is the most efficient.

'''


from collections import deque
from random import shuffle

class Node:
    def __init__(self, state, goal_state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.goal_state = goal_state

    def generate_children(self):
        # Find the position of the empty tile
        row, col = self.state.index(None) // 3, self.state.index(None) % 3

        # Generate child nodes by swapping the empty tile with its neighbors
        for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + drow, col + dcol
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = self.state[:]
                new_state[row * 3 + col], new_state[new_row * 3 + new_col] = new_state[new_row * 3 + new_col], new_state[row * 3 + col]
                self.children.append(Node(new_state, self.goal_state, self))

    def is_goal(self):
        return self.state == self.goal_state

    def print_path(self):
        path = [self]
        while path[-1].parent is not None:
            path.append(path[-1].parent)
        for node in reversed(path):
            print(node.state[:3])
            print(node.state[3:6])
            print(node.state[6:])
            print()
            
    def heuristic(self):
        # Compute the number of tiles that are in the correct position
        count = 0
        for i in range(1, 9):
            if self.state.index(i) == i - 1:
                count += 1
        return count
    
    
class SearchTree:
    
    def __init__(self, start_state, goal_state):
        self.start_node = Node(start_state, goal_state)
        self.goal_state = goal_state
        
    def depth_first_search(self):
        stack = [self.start_node]
        visited = set()

        while stack:
            node = stack.pop()
            if node.is_goal():
                node.print_path()
                return
            visited.add(tuple(node.state))
            node.generate_children()
            for child in node.children:
                if tuple(child.state) not in visited:
                    stack.append(child)
                    visited.add(tuple(child.state))
                    
    def breadth_first_search(self):
        queue = deque([self.start_node])
        visited = set()

        while queue:
            node = queue.popleft()
            if node.is_goal():
                node.print_path()
                return
            visited.add(tuple(node.state))
            node.generate_children()
            for child in node.children:
                if tuple(child.state) not in visited:
                    queue.append(child)

    def hill_climbing_search(self):
            current_node = self.start_node
            while True:
                if current_node.is_goal():
                    current_node.print_path()
                    return
                current_score = current_node.heuristic()
                best_score = current_score
                best_node = current_node
                for child in current_node.children:
                    child_score = child.heuristic()
                    if child_score > best_score:
                        best_score = child_score
                        best_node = child
                if best_score <= current_score:
                    # We have reached a local maximum
                    # Restart with a new random initial state
                    start_state = [1, 2, 3, 4, 5, 6, 7, 8, None]
                    shuffle(start_state)
                    current_node = Node(start_state, self.goal_state)
                else:
                    current_node = best_node
                    
    def beam_search(self, k=2, max_iterations=1000):
        # Initialize the beam with the start node
        beam = [self.start_node]
        iterations = 0
        
        while beam and iterations < max_iterations:
            # Print the current beam
            print("Current beam:")
            for node in beam:
                print(node.state)
            print()
            
            # Generate children for all nodes in the beam
            children = []
            for node in beam:
                node.generate_children()
                children.extend(node.children)
            
            # Sort the children by their heuristic score
            children.sort(key=lambda node: node.heuristic(), reverse=True)
            
            # Check if any of the children is the goal node
            for child in children:
                if child.is_goal():
                    child.print_path()
                    return
                
            # Select the top k children to be the new beam
            new_beam = children[:k]

            # Check if the new beam is the same as the old beam
            if new_beam == beam:
                print("Beam search is stuck in a loop")
                return
            
            beam = new_beam
            iterations += 1
        
        print("Maximum number of iterations reached")
            
    def main(self):
        self.depth_first_search()
        self.breadth_first_search()
        self.hill_climbing_search()
        self.beam_search()
            
if __name__ == "__main__":
    start_state = [1, 4, 3, 7, 8, None, 6, 2, 5]
    goal_state = [1, 2, 3, 8, None, 4, 7, 6, 5]
    search_tree = SearchTree(start_state, goal_state)
    search_tree.main()