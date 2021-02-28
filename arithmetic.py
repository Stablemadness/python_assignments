import re


# takes in strings does the maths
def stringMath(num1, num2, op):
    answer = 0
    if op == '+':
        answer = int(num1) + int(num2)
    elif op == '-':
        answer = int(num1) - int(num2)
    else:
        raise Exception('Error: Op must be "+" or "-"')
    return answer


def arithmetic_arranger(probs, ans=False):
    Answers = ans
    each = []
    lenlist = []
    opList = []
    tL = list()
    bL = list()

    if len(probs) > 5:
        raise Exception('Error: Too many problems')
    for s in probs:
        each.append(s.split())
# check for letters in numbers
    index = 0
    for e in each:
        longest = 0
        for part in e:
            if len(part) > longest:
                longest = len(part)
        lenlist.append(longest)

    for i in range(len(each)):
        if re.search('\D', each[i][0]) is not None:
            raise Exception('Error: Numbers must only contain digits.')
        elif re.search('\D', each[i][2]) is not None:
            raise Exception('Error: Numbers must only contain digits.')


#    print('Len List before add 2: ', lenlist)

    for line in probs:
        op = re.findall('.* ([+-])', line)

        if len(op) < 1:
            raise Exception('Error: Operator must be "+" or "-"')
        else:
            opList.append(op[0])
# construct printable lines
    topLine = ''
    botLine = ''

    for index in range(len(lenlist)):
        lenlist[index] += 2
        topLine = topLine + ' '*(lenlist[index] - len(each[index][0])) + each[index][0] + ' '*4
        botLine = botLine + opList[index] + ' '*(lenlist[index] - len(each[index][2]) - 1) + each[index][2] + ' '*4

    topLine = topLine.rstrip()
    botLine = botLine.rstrip()
#    print(topLine)
#    print(botLine)
#   make dashes
    dashes = ''
    for i in range(len(lenlist)):
        dashes = dashes + '-'*lenlist[i] + ' '*4
#    print(dashes)
    dashes = dashes.rstrip()
    for s in probs:
        s.strip()
        top = re.findall('^[0-9]*', s)
        tL.append(top[0])
        bot = re.findall('.*\s.* ([0-9]+)', s)
        bL.append(bot[0])
        if len(top[0]) < 1 or len(bot[0]) < 1:
            raise Exception('Error: Numbers must only contain digits.')
        elif len(top[0]) > 4 or len(bot[0]) > 4:
            raise Exception('Error: Numbers cannot be more than four digits.')

# get answers if asked for
# build return string
    returnstring = topLine + '\n' + botLine + '\n' + dashes
#    print(returnstring)
    if Answers is True:
        answerstring = ''
        for n in range(len(lenlist)):
            ans = stringMath(tL[n], bL[n], opList[n])
            answerstring = answerstring + ' '*(lenlist[n] - len(str(ans))) + str(ans) + ' '*4
#        print(answerstring)
        returnstring = returnstring + '\n' + answerstring.rstrip()
        return returnstring
    else:
        return returnstring


listofstrings = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]

#arithmetic_arranger(listofstrings, True)
#print()
#arithmetic_arranger(listofstrings)
#print()
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print()
#arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

x = arithmetic_arranger(["3a3 + 5"], True)
print(x)
#arithmetic_arranger(["35552 + 8", "1 - 3801", "9999 + 9999", "523 * 49"], True)
