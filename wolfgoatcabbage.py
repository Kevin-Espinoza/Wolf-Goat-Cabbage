
from operator import truediv
from unittest import result
from search import *


class WolfGoatCabbage(Problem):
    def __init__(self, initial=('F','G','W','C'), goal=()):
        super().__init__(frozenset(initial), frozenset(goal))

    def goal_test(self, state):
        return True if state==set(self.goal) else False

    def result(self, state, action):
        # Set the given state and action to sets for easy manipulation
        state = set(state)
        action = set(action)

        if('F' in state and action.issubset(state)):
            state = state-action
        elif(action.issubset(state)):
            state.remove(action)
        elif('F' in state):
            state.remove('F')
        else:
            state=state.union(action)
            state.add('F')

        # Must return a frozen set since hashable datatype is required
        return frozenset(state)


    def actions(self, state):
        # Set the given state to a set for easy manipulation
        state=set(state)

        # Algo to solve the W-G-C problem 
        possible_actions = [{'F'}, {'G','F'}, {'W','F'}, {'C','F'}] 
        if state == {'F', 'G', 'W', 'C'}:
            possible_actions = [{'F','G'}]
        elif state == {'F', 'C', 'W'}:
            possible_actions = [{'F', 'W'}, {'F','C'}]
        elif state == {'F', 'G', 'W'}:
            possible_actions = [{'F','W'}]
        elif state == {'W', 'C'}:
            possible_actions = [{'F'}]
        elif state == {'W', 'G'}:
            possible_actions = [{'F'}]
        elif state == {'F', 'G'}:
            possible_actions = [{'F', 'G'}]
        elif state == {'F', 'C'}:
            possible_actions = [{'F'}, {'F','C'}] 
        elif state == {'F', 'W'}:
            possible_actions = [{'F'}, {'F','W'}]
        elif state == {'W'}:
            possible_actions = [{'F', 'G'}]
        elif state == {'G'}:
            possible_actions = [{'F'}, {'F','W'}, {'F','C'}]
        elif state == {'C'}:
            possible_actions = [{'F','G'}]
        elif state == {'F'}:
            possible_actions = [{'F'}]
            
        return possible_actions


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)