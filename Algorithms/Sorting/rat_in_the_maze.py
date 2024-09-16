def printmazehelper(x,y,maze,n,solution):
    if x==n-1 and y==n-1:
        solution[x][y]=1
        print(solution)
        solution[x][y]=0
        return
    if x<0 or y<0 or x>=n or y>=n or solution[x][y]==1 or maze[x][y]==0:
        return
    solution[x][y]=1
    printmazehelper(x+1,y, maze, n, solution)
    printmazehelper(x,y+1, maze, n, solution)
    printmazehelper(x-1,y, maze, n, solution)
    printmazehelper(x,y-1, maze, n, solution)
    solution[x][y]=0
    return

def printmaze(maze):
    n=len(maze)
    solution=[[0 for j in range(n)] for i in range (n)]
    printmazehelper(0,0,maze,n,solution)

n=int(input("Enter the matrix row "))
maze=[]
for i in range(n):
    row=[int(ele) for ele in input("Enter the matrix element ").split()]
    maze.append(row)

printmaze(maze)


"""
OUTPUT

Enter the matrix row 4
Enter the matrix element 1 1 1 1
Enter the matrix element 1 0 1 1
Enter the matrix element 1 1 0 1
Enter the matrix element 1 1 1 1
[[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1]]
[[1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 1]]
[[1, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
[[1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]

"""
