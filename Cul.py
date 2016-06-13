def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1


def readDivision(line, index):
    token = {'type': 'DIVISION'}
    return token, index + 1




def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMultiply(line, index)
        elif line[index] == '/':
            (token, index) = readDivision(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    #print tokens
    return tokens



def evaluateMultiplyAndDivide(tokens):
    tmp = []
    index = 0
    answer = 1
    if len(tokens) == 1:
        return tokens
    if index == 0:
        tmp.append({'type' : 'NUMBER', 'number': tokens[index]['number']})
        index = index+1

    while index < len(tokens):
        #print 'while in'
        #print index
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MULTIPLY':
                lastnumber = tmp[len(tmp)-1]['number']
                last = tmp.pop()
                lastnumber *= tokens[index]['number']
                tmp.append({'type' : 'NUMBER', 'number': lastnumber})
            elif tokens[index - 1]['type'] == 'DIVISION':
                lastnumber = t[len(t)-1]['number']
                last = t.pop()
                lastnumber /= tokens[index]['number']
                tmp.append({'type' : 'NUMBER', 'number': lastnumber})
            elif tokens[index - 1]['type'] == 'MINUS':
                tmp.append({'type': 'MINUS'})
                tmp.append({'type' : 'NUMBER', 'number': tokens[index]['number']})
            elif tokens[index - 1]['type'] == 'PLUS':
                tmp.append({'type': 'PLUS'})
                tmp.append({'type' : 'NUMBER', 'number': tokens[index]['number']})
            else:
                print 'pre Invalid syntax'
               
        index += 1 
  
    return tmp

def evaluatePlusAndMinus(t):
    tmp.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' tmp
    #print tmp
    answer = 0
    index = 1
    while index < len(tmp):
        if tmp[index]['type'] == 'NUMBER':
            if tmp[index - 1]['type'] == 'PLUS':
                answer += tmp[index]['number']
            elif tmp[index - 1]['type'] == 'MINUS':
                answer -= tmp[index]['number']
                
        index += 1
    return answer




while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    tmp = evaluateMultiplyAndDivide(tokens)
    answer = evaluatePlusAndMinus(tmp)
    print "answer = %f\n" % answer
