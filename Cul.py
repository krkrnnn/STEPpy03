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



def preEvaluate(tokens):
    t = []
    index = 0
    if len(tokens) == 1:
        return tokens
    while index < len(tokens) - 2:
        #print 'while in'
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index + 1]['type'] == 'MULTIPLY':
                answer = tokens[index]['number']*tokens[index+2]['number']
                # add answer to t[]
                t.append({'type': 'NUMBER', 'number': answer})
                index = index + 2
            elif tokens[index + 1]['type'] == 'DIVISION':
                print 'div'
                print index
                answer = tokens[index]['number']/tokens[index+2]['number']
                # add answer to t[]
                t.append({'type': 'NUMBER', 'number': answer})
                index = index + 2
            elif tokens[index + 1]['type'] == 'MINUS':
                t.append({'type' : 'NUMBER', 'number': tokens[index]['number']})
                t.append({'type': 'MINUS'})
                index = index + 2
            elif tokens[index + 1]['type'] == 'PLUS':
                #print 'plusok'
                t.append({'type' : 'NUMBER', 'number': tokens[index]['number']})
                t.append({'type': 'PLUS'})
               
                index = index + 2
            else:
                print 'pre Invalid syntax'
                
    t.append({'type' : 'NUMBER', 'number' : tokens[len(tokens)-1]['number']})    
    return t

def evaluate(t):
    print t
    answer = 0
    t.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(t):
        if t[index]['type'] == 'NUMBER':
            if t[index - 1]['type'] == 'PLUS':
                answer += t[index]['number']
            elif t[index - 1]['type'] == 'MINUS':
                answer -= t[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer




while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    t = preEvaluate(tokens)
    answer = evaluate(t)
    print "answer = %f\n" % answer
