
from operator import truediv
from unittest import result
from search import *
# YOUR CODE GOES HERE


class WolfGoatCabbage(Problem):
    def __init__(self, initial=('F','G','W','C'), goal=()):
        self.initial = frozenset(initial)
        self.goal = frozenset(goal)
        # super().__init__(self.initial, self.goal)

    def goal_test(self, state):
        # print('\nGOAL TEST - STATE: ', state)
        # print('GOAL STATE: ', self.goal)
        if state==set(self.goal):
            return True
        else:
            return False

    # This is a helper function that checks if the farmer is in the current state
    def farmer(self, state):
        if('F' in state):
            return True
        else:
            return False

    def result(self, state, action):
        state = set(state)
        action = set(action)
        # print('\nSTATE: ', state)
        # print('ACTION: ', action)

        test = self.farmer(state)
        if(test and action.issubset(state)):
            state = state-action
            # state.remove('F')
            # print('NEW STATE: ', state)
        elif(action.issubset(state)):
            # state.add('F')
            state.remove(action)
            # print('NEW STATE: ', state)
        elif(test):
            state.remove('F')
            # print('NEW STATE: ', state)
        else:
            state.union(action)
            state.add('F')
            # print('NEW STATE: ', state)
            
        return frozenset(state)


    def actions(self, state):
        # print('ACTIONS')
        # print('\n')
        state_temp=set(state)
        # print("INITIAL is:", self.initial)
        print('STATE: ', state)

        possible_actions = [{'F'}, {'G','F'}, {'W','F'}, {'C','F'}]
        if state_temp == {'F', 'G', 'W', 'C'}:
            possible_actions = [{'G','F'}]
        elif state_temp == {'F', 'C', 'W'}:
            possible_actions = [{'W','F'}]
        elif state_temp == {'F', 'G', 'W'}:
            possible_actions = [{'W','F'}]
        elif state_temp == {'W', 'C'}:
            possible_actions = [{'F'}, {'G','F'}]
        elif state_temp == {'W', 'G'}:
            possible_actions = [{'F'}, {'C','F'}]
        elif state_temp == {'F', 'G'}:
            possible_actions = [{'G','F'},]
        elif state_temp == {'F', 'C'}:
            possible_actions = [{'F'}, {'C','F'}] 
        elif state_temp == {'F', 'W'}:
            possible_actions = [{'F'}, {'W','F'}]
        elif state_temp == {'W'}:
            possible_actions = [{'F'}]
        elif state_temp == {'G'}:
            possible_actions = [{'F'}, {'W','F'}, {'C','F'}]
        elif state_temp == {'C'}:
            possible_actions = [{'G','F'}]
        elif state_temp == {'F'}:
            possible_actions = [{'F'}]
        return possible_actions


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)