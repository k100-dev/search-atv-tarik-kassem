from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):
    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        frontier = [(initial, 0)]
        best_depth = {initial: 0}
        expanded, generated, maximum = 0, 1, 1
        while frontier:
            state, depth = frontier.pop()
            if depth != best_depth[state]:
                continue
            if state.is_goal:
                return SearchResult(state, expanded, generated, maximum, depth)
            if depth >= self.depth_limit:
                continue
            expanded += 1
            for child in reversed(state.neighbors()):
                next_depth = depth + 1
                if next_depth < best_depth.get(child, float('inf')):
                    best_depth[child] = next_depth
                    frontier.append((child, next_depth))
                    generated += 1
            maximum = max(maximum, len(frontier))
        return SearchResult(None, expanded, generated, maximum)
