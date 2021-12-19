

class DFS:
    # https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
    def __init__(self, graph) -> None:
        self.visited_nodes = set()
        self.graph = graph

    
    def dfs(self, node: str) -> None:
        if node not in self.visited_nodes:
            print(node)
            self.visited_nodes.add(node)
            neighbours = self.graph[node]
            for neighbour in neighbours:
                self.dfs(neighbour)

    
    def depth_first_search(self, node: str) -> None:
        self.visited_nodes.clear()
        self.dfs(node)
   

if __name__ == "__main__":

    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }

    dfs = DFS(graph)
    dfs.depth_first_search("A")


