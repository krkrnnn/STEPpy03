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
    return tokens





def evaluate(tokens):
    answer = 0
    answer1 = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1

    #array which is finished * and /
    t = []
    t.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' t
    tindex = 1

    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MULTIPLY':
                answer1 *= tokens[index]['number']
                t[tindex] = answer1
                t[tindex]['type'] = 'NUMBER'
                tindex += 1
            elif tokens[index - 1]['type'] == 'DIVISION':
                answer1 /= tokens[index]['number']
                t[tindex] = answer1
                t[tindex]['type'] = 'NUMBER'
                tindex += 1
            elif tokens[index - 1]['type'] == 'PLUS':
                t[tindex]['type'] = 'PLUS'
                tindex += 1
            elif tokens[index - 1]['type'] == 'MINUS':
                t[tindex]['type'] = 'MINUS'
                tindex += 1
            else:
                
                print 'Invalid syntax'
        index += 1

   
    tindex = 1

    while tindex < len(t):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer



while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print "answer = %f\n" % answer
