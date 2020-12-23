cases = int(input())
def location(name, seq):
    for z in range(len(seq)):
        if name in seq[z]:
            return z
    return False

def empty(seq):
    final = []
    for z in seq:
        if z != []:
            final.append(z)
    return final
    

def reverse(seq):
    new = []
    for i in range(len(seq)):
        new.append(seq[-i-1])
    return new
for x in range(cases):
    names = []
    setup = []
    people = int(input())
    for i in range(people):
        hold = input()
        names.append(hold)
        setup.append([])
    names = reverse(names)
    spot = -1
    for i in names:
        save = location(i,setup)
        if save is not False:
            spot = save
        else:
            spot += 1
            setup[spot].append(i)
#    print(setup)

    setup = empty(setup)
    count = (len(setup) - 1) * 20
    print(len(names) * 10 - count)



