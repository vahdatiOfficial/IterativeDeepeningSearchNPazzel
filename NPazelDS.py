from queue import LifoQueue
class Problem:
    def __init__(self,initialState,goalState) -> None:
        self.initialState = initialState.split(" ")
        self.goalState = goalState.split(" ")
class Node:
    def __init__(self,father,action,root,depth) -> None:
        self.father = father
        self.action = action
        self.depth = depth
        self.root = list(root)
def problemActions(node):
    index = node.root.index('0')
    lis = []
    if((index - n) > -1):
        lis.append("U")
    if((index + 1) % n != 0):
        lis.append("R")
    if((index + n) < (n**2)):
        lis.append("D")
    if(index % n != 0):
        lis.append("L")
    return lis
def Expand(node):
    children =[]
    actions = problemActions(node)
    for x in actions:
        children.append(newChildNode(node,x))
    return children
def newChildNode(node,action):
    index = node.root.index('0')
    temp = node.root
    if(action == "U"):
        temp[index] , temp[index - n] = temp[index - n] , temp[index]
        node1 = Node(node,action,temp,node.depth + 1)
        temp[index - n] , temp[index] = temp[index] , temp[index - n]
        return node1
    if(action == "D"):
        temp[index] , temp[index + n] = temp[index + n] , temp[index]
        node1 = Node(node,action,temp,node.depth + 1)
        temp[index + n] , temp[index] = temp[index] , temp[index + n]
        return node1
    if(action == "R"):
        temp[index] , temp[index + 1] = temp[index + 1] , temp[index]
        node1 = Node(node,action,temp,node.depth + 1)
        temp[index + 1] , temp[index] = temp[index] , temp[index + 1]
        return node1
    if(action == "L"):
        temp[index] , temp[index - 1] = temp[index - 1] , temp[index]
        node1 = Node(node,action,temp,node.depth + 1)
        temp[index - 1] , temp[index] = temp[index] , temp[index - 1]
        return node1
def solution(node):
    def slu(nodes):
        lia = ""
        if(nodes.father is not None):
            n = nodes.father
            lia = slu(n)
        if(nodes.action != None):
            lia += nodes.action + " "
        return lia
    soloList = slu(node)
    soloList = soloList[:-1]
    return soloList
def IsCycle(node):
    node1 = node
    while node1.father != None:
        if(node.root == node1.father.root):
            return True
        node1 = node1.father
    return False
def DepthLimitedSearch(problem,limit):
    i = 0
    nodeState = Node(None,None,problem.initialState,0)
    frontier = LifoQueue()
    frontier.put(nodeState)
    result = failure
    while not frontier.empty():
        node = frontier.get()
        if (problem.goalState == node.root):
            return solution(node) , i
        if(node.depth > limit):
            result = cutoff
        elif(not IsCycle(node)):
            for child in Expand(node):
                frontier.put(child)
            i += 1
    return result , i
def IterativeDeepeningSearch(problem):
    depth = 0
    expand = 0
    while True:
        result , i = DepthLimitedSearch(problem,depth)
        expand += i
        if(result != cutoff):
            return result , expand 
        depth += 1
global cutoff
global failure
global n
cutoff = "cutoff"
failure = "failure"
n = int(input())
initialState = input()
goalState = input()
problem = Problem(initialState,goalState)
solution = IterativeDeepeningSearch(problem)
if(solution[0] == failure):
    print(solution[1])
    print("No solution found")

else:
    print(solution[1])
    print(solution[0])
