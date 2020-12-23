cases = int(input())
def remove(word):
    final = []
    for i in word:
        if i != "-":
            final.append(i)
    return final


def replace(word):
    result = []
    for i in word:
        if i.isalpha() == True:
            if i == "A" or i == "B" or i == "C":
                result.append("2")
            elif i == "D" or i == "E" or i == "F":
                result.append("3")
            elif i == "G" or i == "H" or i == "I":
                result.append("4")
            elif i == "J" or i == "K" or i == "L":
                result.append("5")
            elif i == "M" or i == "N" or i == "O":
                result.append("6")
            elif i == "P" or i == "Q" or i == "R" or i == "S":
                result.append("7")
            elif i == "T" or i == "U" or i == "V":
                result.append("8")
            elif i == "W" or i == "X" or i == "Y" or i == "Z":
                result.append("9")
        else:
            result.append(i)
    return result

def inserthype(word):
    word.insert(3,"-")
    word.insert(7 , "-")
    return word



for i in range(cases):
    hold = input()
    wordnum = list(hold)
    wordnum = remove(wordnum)
    wordnum = wordnum[:10]
    wordnum = replace(wordnum)
    wordnum = inserthype(wordnum)
    print(*wordnum, sep = "")
