from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):
    def search(self, initial: State) -> SearchResult:
        frontier = deque([(initial, 0)])
        visited = {initial}
        expanded, generated, maximum = 0, 1, 1
        while frontier:
            state, depth = frontier.popleft()
            if state.is_goal:
                return SearchResult(state, expanded, generated, maximum, depth)
            expanded += 1
            for child in state.neighbors():
                if child not in visited:
                    visited.add(child)
                    frontier.append((child, depth + 1))
                    generated += 1
            maximum = max(maximum, len(frontier))
        return SearchResult(None, expanded, generated, maximum)
