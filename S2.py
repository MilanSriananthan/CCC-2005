dimen = input()
dimen = dimen.split(" ")
col = int(dimen[0])
row = int(dimen[1])
current = [0,0]
def makenum(seq):
    result = []
    for i in seq:
        result.append(int(i))
    return result

def horizontal(move):
    test = current[0]
    if test + move > col:
        current[0] = col
    elif test + move < 0:
        current[0] = 0
    else:
        current[0] += move
    return current

def vertical(move):
    test = current[1]
    if test + move > row:
        current[1] = row
    elif test + move < 0:
        current[1] = 0
    else:
        current[1] += move
    return current


while True:
    task = input()
    task = task.split(" ")
    task = makenum(task)
    if task == [0,0]:
        break
    current = vertical(task[1])
    current = horizontal(task[0])
    print(*current, sep = " ")







'''
line = []
for i in range(col):
    line.append(0)

for i in range(row):
'''