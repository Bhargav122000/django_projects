# functions for Calculator
def isOperator(term):
    operators = [ '+', '-', '*', '/', '^' ]
    return term in operators

def isParentheses(term):
    parentheses = [ '(', ')' ]
    return term in parentheses

def getPrecedence(operator):
    precedence = -1
    if operator == '+' or operator == '-':
        precedence = 1
    elif operator == '*' or operator == '/':
        precedence = 2
    elif operator == '^':
        precedence = 3
    return precedence

def convertToPostfix(expression):
    operatorStack = []
    postfixExpression = ''
    for term in expression:
        if term == ' ':
            continue
        elif isOperator(term):
            if len(operatorStack) == 0:
                operatorStack.append(term)
            else:
                topTerm = operatorStack[len(operatorStack) - 1]
                if getPrecedence(term) > getPrecedence(topTerm):
                    operatorStack.append(term)
                else:
                    postfixExpression += topTerm
                    postfixExpression += ' '
                    operatorStack.remove(topTerm)
                    operatorStack.append(term)
        elif isParentheses(term):
            if term == '(':
                operatorStack.append(term)
            else:
                i = len(operatorStack) - 1
                while len(operatorStack) > 0 and operatorStack[i] != '(':
                    postfixExpression += operatorStack[i]
                    postfixExpression += ' '
                    operatorStack.pop()
                    i -= 1
                if len(operatorStack) > 0 and operatorStack[i] == '(':
                    operatorStack.pop()
        else:
            postfixExpression += term
            postfixExpression += ' '

    while len(operatorStack) > 0:
        topTerm = operatorStack[len(operatorStack) - 1]
        operatorStack.pop()
        if topTerm != '(':
            postfixExpression += topTerm + ' '
    return postfixExpression

def computeOperator(operator, operand1, operand2):
    value = None
    if operator == '+':
        value = operand1 + operand2
    elif operator == '-':
        value = operand1 - operand2
    elif operator == '*':
        value = operand1 * operand2
    elif operator == '/':
        value = operand1 / operand2
    elif operator == '^':
        value = operand1 ** operand2
    return value

def evaluatePostfix(postfix):
    operandStack = []
    value = None
    for term in postfix:
        if isOperator(term):
            index = len(operandStack) - 1
            operand2 = float(operandStack[index])
            operandStack.pop()
            index -= 1
            operand1 = float(operandStack[index])
            operandStack.pop()
            index -= 1
            tempValue = computeOperator(term, operand1, operand2)
            operandStack.append(tempValue)
        else:
            operandStack.append(float(term))
    value = operandStack[0]
    if (value - int(value)) == 0:
        value = int(value)
    else:
        value = round(value, 10)
    return value

def calculate(input):
    print('infix expression: ', input)
    postfix = convertToPostfix(input.strip().split(' '))
    print('postfix expression: ', postfix)
    value = evaluatePostfix(postfix.strip().split(' '))
    print('value of expression: ', value)
    return value
