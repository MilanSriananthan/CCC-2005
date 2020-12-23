
cases = int(input())
def rank(num, seq):
    for i in range(len(seq)):
        if seq[i] < num:
            seq.insert(i, num)
            break
board = []
first = int(input())
board.append(first)
ranking = [1]
for i in range(cases - 1):
#    print(board)
    score = int(input())
    for x in range(len(board)):
        if board[x] < score:
            board.insert(x, score)
            ranking.append(x + 1)
            break
        if x == len(board) - 1:
            board.append(score)
            ranking.append(x + 2)

total = sum(ranking)
answer = total/len(ranking)
print("%.2f" % round(answer, 2))