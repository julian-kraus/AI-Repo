# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def minimize_path(problem, path, type):
    new_path = []
    node = get_end_of_transition(path[len(path) - 1], type)
    counter = len(path)
    while problem.getStartState() != node:
        if counter == 0:
            print("counter too small")
            return new_path
        counter -= 1

        if get_end_of_transition(path[counter], type) == node:
            new_path.insert(0, path[counter][1])
            node = get_start_of_transition(path[counter], type)

    return new_path

def get_start_of_transition(node, type):
    if type == "graph":
        start = str(node[1]).split(":")[1]
        return str(start).split("-")[0]
    else:
        if node[1] == "South":
            return tuple((node[0][0], node[0][1] - 1))
        elif node[1] == "North":
            return tuple((node[0][0], node[0][1] + 1))
        elif node[1] == "West":
            return tuple((node[0][0] + 1, node[0][1]))
        elif node[1] == "East":
            return tuple((node[0][0] - 1, node[0][1]))

def get_end_of_transition(node, type):
    if type == "graph":
        return str(node[1]).split(">")[1]
    else:
        return node[0]

def search_algorithm(struct, problem, type):
    struct.push(problem.getStartState())
    path = []
    visited_node = []

    while not struct.isEmpty():
        node = struct.pop()
        if problem.getStartState() == node:
            end_node = node
        else:
            end_node = get_end_of_transition(node, type)
            path.append(node)

        visited_node.append(end_node)

        if problem.isGoalState(end_node):
            return minimize_path(problem, path, type)
        successors = problem.getSuccessors(end_node)
        for succ in successors:
            if get_end_of_transition(succ, type) not in visited_node:
                struct.push(succ)

    return " ".join(path)

def get_type(node):
    if isinstance(node, str):
        return "graph"
    else:
        return "grid"

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    return search_algorithm(util.Stack(), problem, get_type(problem.getStartState()))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return 10/0 # search_algorithm(util.Queue(), problem, get_type(problem.getStartState()))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
