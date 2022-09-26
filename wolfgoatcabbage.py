
from operator import truediv
from unittest import result
from search import *
# YOUR CODE GOES HERE


class WolfGoatCabbage(Problem):
    def __init__(self, initial={'F','G','W','C'}, goal=('F','G','W','C')):
        self.initial = tuple(initial)
        self.goal = goal

    def goal_test(self, state):
        # return True if set(state)==set(self.goal) else False
        if set(state)==set(self.goal) and 'F' not in self.initial:
            print("FINAL STATE", state)
            return True
        else:
            False

    def result(self, state, action):
        state=set(state)
        if('F' in state):
            state.remove('F')
        else:
            state.add('F')

        if(action != 'F'):
            if(action in state):
                state.remove(action)
            else:
                state.add(action)

        return tuple(state)

    def actions(self, state):
        # Make a temp state for easy manipulation
        state_temp=set(state)
        # print("\nSTATE", state)

        valid = set()
        if state_temp == {'F','G','W','C'}:
            valid.add('F')
            valid.add('G')
        elif state_temp == {'F', 'G', 'W'}:
            valid.add('F')
            valid.add('W')
        elif state_temp == {'F', 'C', 'W'}:
            valid.add('F')
            valid.add('C')
        elif state_temp == {'F', 'G', 'C'}:
            valid.add('F')
            valid.add('C')
        elif state_temp == {'F', 'G'}:
            valid.add('F')
            valid.add('C')
            valid.add('G')
        elif state_temp == {'W'}:
            valid.add('F')
            valid.add('G')
        else:
            valid.add('F')

        self.initial=set(self.initial)

        if(valid.issubset(self.initial)):
            self.initial=self.initial-valid
        else:
            self.initial.union(valid)

        self.initial=tuple(self.initial)
        # Revert state back to tuple
        # state=tuple(state)

        # Override state_temp to be a copy of the object's initial state as a set
        # print("LHS", self.initial)
        # init_temp=set(self.initial)
        # print("VALID", valid)
        # print("INIT_TEMP", init_temp)
        # print(valid.issubset(init_temp))
        # if set(state) == init_temp and valid.issubset(init_temp):
        #     init_temp = tuple(init_temp-valid)
        #     print("LHS is now", init_temp)
        # elif set(state) == init_temp:
        #     init_temp = tuple(init_temp.union(valid))
        #     print("LHS is now ", init_temp)
        # else:
        #     pass

        # self.initial=init_temp
        return list(valid) 


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc)
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)