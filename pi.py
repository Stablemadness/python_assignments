import re


def arithmetic_arranger(problems, answers=False):
    each = []
    opList = []
    lenList = list()

    if len(problems) > 4:
        raise Exception('Error: Too many problems.')

    for string in problems:
        x = string.split()
#        print(x)
# Check for digits and digit length
        if re.search('\D',x[0]) is not None:
            raise Exception('Error: Numbers must only contain digits.')
        elif re.search('\D',x[2]) is not None:
            raise Exception('Error: Numbers must only contain digits.')
        elif len(x[0]) > 4 or len(x[2]) > 4:
            raise Exception('Error: Numbers cannot be more than four digits.')

# Check operator
        if x[1] == '+':
            opList.append(x[1])
        elif x[1] == '-':
            opList.append(x[1])
        else:
            raise Exception('Error: Operator must be "+" or "-"')
# If problem is okay append the parts to a list
        each.append(x)

# Get longest number in problem for spacing
#    index = 0
    for prob in each:
        longest = 0
        for string in prob:
            if len(string) > longest:
                longest = len(string)
        lenList.append(longest+2)

# Make top and bottom lines
    topLine = ""
    botLine = ""

    for index in range(len(each)):
        num1 = each[index][0]
        num2 = each[index][2]
        topLine = topLine + ' '*(lenList[index] - len(num1)) + num1 + ' '*4
        botLine = botLine + opList[index] + ' '*(lenList[index] - (len(num2)+1)) + num2 + ' '*4
# Make dash line
    dashes = ''
    for n in range(len(each)):
        dashes = dashes + "-"*lenList[n] + ' '*4

# build string to return
    topLine = topLine.rstrip()
    botLine = botLine.rstrip()
    arranged_problem = topLine + '\n' + botLine + '\n' + dashes.rstrip()

# answers needed?
    answerLine = ""

    if answers is True:
        ansList = []
        for p in range(len(each)):
            ans = int(each[p][0])
            if opList[p] == '+':
                ans += int(each[p][2])
            else:
                ans -= int(each[p][2])
            ansList.append(ans)
        for i in range(len(each)):
            answerLine = answerLine + ' '*(lenList[i] - len(str(ansList[i]))) + str(ansList[i]) + ' '*4
        arranged_problem = arranged_problem + '\n' + answerLine.rstrip()
    return arranged_problem

# spaces are lenlist[index] - len(part)

#    print(each)
#    print(opList)
#    print(lenList)
#    print(topLine)
#    print(botLine)
#    print(dashes)
#    print(answerLine)
#arithmetic_arranger(['102 + 33', '634 - 515', '29 + 8'], False)
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print()
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
