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

def init():
    for i in range(1,9):
        for j in range(1,9):
            if feild[i][j] == 4:
                feild[i][j] = 0

def feild_cnt():
    cnt = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if feild[i][j] == 0:
                cnt += 1
    return cnt

def check_flip(sy, sx, turn):
    if feild[sy][sx] != 0:
        return -1
    
    for i in range(len(dy)):
        ny = 0
        nx = 0
        flag = 0
        while True:
            ny += dy[i]
            nx += dx[i] 
            if (0 < sy+ny and sy+ny < 9) and (0 < sx+nx and sx+nx < 9) and (feild[sy+ny][sx+nx] == 0 or feild[sy+ny][sx+nx] == 4):
                break

            if feild[sy+ny][sx+nx] == 3:
                break
            if flag == 1 and feild[sy+ny][sx+nx] == turn:
                return 1
            elif feild[sy+ny][sx+nx] == 3 - turn:
                flag = 1
                continue
    return -1

def flip(sy, sx, turn):
    feild[sy][sx] = turn
    for i in range(len(dy)):
        ny = 0
        nx = 0
        flag = 0
        while True:
            ny += dy[i]
            nx += dx[i]
            if feild[sy+ny][sx+nx] == 3:
                break
            if flag == 1 and feild[sy+ny][sx+nx] == turn:
                break
            elif feild[sy+ny][sx+nx] == 3 - turn:
                flag = 1
                feild[sy+ny][sx+nx] = turn
                continue

def display():
    print("  1 2 3 4 5 6 7 8")
    for i in range(1, 9):
        print(i, end=" ")
        for j in range(1, 9):
            if j == 8:
                if feild[i][j] == 0:
                    print('⬜︎')
                elif feild[i][j] == 1:
                    print('●')
                elif feild[i][j] == 2:
                    print('○') 
                elif feild[i][j] == 4:
                    print('■')
            else:
                if feild[i][j] == 0:
                    print('⬜︎', end=" ")
                elif feild[i][j] == 1:
                    print('●', end=" ")
                elif feild[i][j] == 2:
                    print('○', end=" ")
                elif feild[i][j] == 4:
                    print('■', end=" ")

def othello():
    turn = 2
    while(True):
        if feild_cnt == 0: break
        init()
        for i in range(1,9):
            for j in range(1,9):
                if check_flip(i,j,turn) == 1:
                    feild[i][j] = 4
        display()
        if turn == 2:
            print("手番は黒です")
        else:
            print("手番は白です")
        print("駒を置く添字を指定してください")
        y = int(input("y座標"))
        x = int(input("x座標"))
        if feild[y][x] == 4:
            flip(y, x, turn)
        elif feild[y][x] == 0:
            print("ここに石は置けません")
            print()
            continue
        turn = 3 - turn
        print()

    black_cnt = 0
    white_cnt = 0
    for i in range(1,9):
        for j in range(1,9):
            if feild[i][j] == 1:
                black_cnt += 1
            elif feild[i][j] == 2:
                white_cnt += 1

    if black_cnt < white_cnt:
        print("白の勝ち")
    else:
        print("黒の勝ち")
        
if __name__ == '__main__':
    othello()
