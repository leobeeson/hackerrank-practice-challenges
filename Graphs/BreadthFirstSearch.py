

class BFS:
    # https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
    def __init__(self, graph) -> None:
        self.graph = graph
        self.visited = []
        self.queue = []


    def bfs(self, node: str) -> None:
        self.visited.append(node)
        self.queue.append(node)

        while self.queue:
            queued_node = self.queue.pop(0)
            print(queued_node, end = " ")

            neighbours = self.graph[queued_node]
            for neighbour in neighbours:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)
    
    def breadth_first_search(self, node: str) -> None:
        self.visited.clear()
        self.queue.clear()
        self.bfs(node)
 

if __name__ == "__main__":

    graph = {
        "A": ["B", "C"],
        "B": ["F", "E"],
        "C": ["D"],
        "D": [],
        "E": ["D"],
        "F": []
    }

    bfs = BFS(graph)
    bfs.breadth_first_search("A")
