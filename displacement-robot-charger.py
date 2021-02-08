# Robot and Charger
from math import sqrt
def movement(x0=0,y0=0):
    axes = {'UP':1,
            'DOWN':-1,
            'LEFT':-1,
            'RIGHT':1,}
    x,y = x0,y0
    print("Enter sequence of movements...")
    print(*axes,"end of legend...",sep='[] --- ')
    steps = int(input("movement sequence length: "))
    for _ in range(steps):
        axis,length = input().split()
        if axis in ['LEFT','RIGHT']:
            x = x + axes[axis]*float(length)
        elif axis in ['UP', 'DOWN']:
            y = y + axes[axis]*float(length)
    print(f"Robot displacement from ({x0},{y0}) to ({x},{y})")
    print(f"Displacement = {displacement(x0,y0,x,y)} units")
    return 'Done...'

def displacement(x0,y0,x,y):
    return sqrt(((x-x0)**2)+((y-y0)**2))

if __name__ == "__main__":
    x0,y0 = map(int , input("Robot start-point coordinates x,y = ").split(','))
    print(movement(x0,y0))
