feild = [
         [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
         [3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [3, 0, 0, 0, 1, 2, 0, 0, 0, 3],
         [3, 0, 0, 0, 2, 1, 0, 0, 0, 3],
         [3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]

dy = [-1, -1, -1, 0, 1, 1,  1,  0]
dx = [-1,  0,  1, 1, 1, 0, -1, -1]

def sand(sy, sx, turn):
    if feild[sy][sx] != 0: return False
    feild[sy][sx] = turn
    for i in range(len(dy)):
        ny = 0
        nx = 0
        while True:
            ny += dy[i]
            nx += dx[i]
            
            if feild[sy+ny][sx+nx] == 3 or feild[sy+ny][sx+nx] == turn:
                break
            elif feild[sy+ny][sx+nx] == 3 - turn:
                continue

        if feild[sy+ny][sx+nx] == turn:
            ny = 0
            nx = 0
            
            while True:
                ny += dy[i]
                nx += dx[i]
                if feild[sy+ny][sx+nx] == turn:
                    break
                elif feild[sy+ny][sx+nx] == 3 - turn:
                    feild[sy+ny][sx+nx] = turn
                    continue

def display():
    print("  1 2 3 4 5 6 7 8")
    for i in range(1, 9):
            print(i, end=" ")
            for j in range(1, 9):
                if j == 8:
                    print(feild[i][j])
                else:
                    print(feild[i][j], end=" ")

def flip(y, x, turn):
    if feild[y][x] == 0:
        feild[y][x] = turn;

def othello():
    turn = 2
    while(True):
        display()
        print("駒を置く添字を指定してください")
        y = int(input("y座標"))
        x = int(input("x座標"))
        sand(y, x, turn)
        turn = 3 - turn
        print()


if __name__ == '__main__':
    othello()
