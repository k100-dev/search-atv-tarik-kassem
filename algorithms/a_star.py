import heapq
from itertools import count
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):
    def heuristic(self, state: State) -> int:
        distance = 0
        for index, tile in enumerate(state.tiles):
            if tile != 0:
                row, col = divmod(index, 3)
                goal_row, goal_col = divmod(tile - 1, 3)
                distance += abs(row - goal_row) + abs(col - goal_col)
        return distance

    def search(self, initial: State) -> SearchResult:
        order = count()
        frontier = [(initial.cost + self.heuristic(initial), next(order), initial, 0)]
        best_cost = {initial: initial.cost}
        expanded, generated, maximum = 0, 1, 1
        while frontier:
            _, _, state, depth = heapq.heappop(frontier)
            if state.cost != best_cost[state]:
                continue
            if state.is_goal:
                return SearchResult(state, expanded, generated, maximum, depth)
            expanded += 1
            for child in state.neighbors():
                if child.cost < best_cost.get(child, float('inf')):
                    best_cost[child] = child.cost
                    priority = child.cost + self.heuristic(child)
                    heapq.heappush(frontier, (priority, next(order), child, depth + 1))
                    generated += 1
            maximum = max(maximum, len(frontier))
        return SearchResult(None, expanded, generated, maximum)
