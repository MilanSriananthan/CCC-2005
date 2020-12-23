boxes = int(input())
def makenum(seq):
    result = []
    for x in seq:
        result.append(int(x))
    return result


grid = []
allboxs = []
alldimen = []
for i in range(boxes):
    dimen = input()
    dimen = dimen.split(" ")
    dimen = makenum(dimen)
    onebox = []
    for z in range(dimen[0]):
        hold = input()
        hold = hold.split(" ")
        hold = makenum(hold)
        onebox.append(hold)
    allboxs.append(onebox)
    alldimen.append(dimen)

rows = 1
col = 1
for i in alldimen:
    rows *= i[0]
    col *= i[1]

for i in range(col):
    .append(0)

for i in range(rows):
    grid += first
print(grid)

print(allboxs)
print(alldimen)
