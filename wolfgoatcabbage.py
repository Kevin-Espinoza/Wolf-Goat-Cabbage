
from operator import truediv
from search import *
# YOUR CODE GOES HERE


class WolfGoatCabbage(Problem):
    def __init__(self, initial={'F','G','W','C'}, goal={''}):
        self.initial = frozenset(initial)
        self.goal = goal

    def goal_test(self, state):
        return True if set(state)==self.goal else False

    def result(self, state, action):
        if(action.issubset(state)):
            state=state-action
        else:
            state=state.union(action)
        return frozenset(state)

    def actions(self, state):
        valid = []
        if state == {'F','G','W','C'}:
            valid.append({'F','G'})
        elif state == {'F', 'G', 'W'}:
            valid.append({'F', 'W'})
        elif state == {'F', 'C', 'W'}:
            valid.append({'F'})
        elif state == {'F', 'G', 'C'}:
            valid.append({'F', 'C'})
        elif state == {'F', 'G'}:
            valid.append({'F', 'G'})
        elif state == {'F', 'C'}:
            valid.append({'F', 'C'})
        elif state == {'F', 'W'}:
            valid.append({'F', 'W'})
        else:
            pass
        valid.append({'F'})
        return valid 


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)