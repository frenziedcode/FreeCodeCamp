import re

def arithmetic_arranger(problems, solve = True) :

    if len(problems) > 5:
        return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    sumx = ""

    for problem in problems :
        operands = problem.split()
        if len(operands) != 3:
            return "Erro: Cada problema deve conter dois operandos e um operador."

        num1 = operands[0]
        symbol = operands[1]
        num2 = operands[2]

        if ( (symbol != '+') and (symbol != '-') ) :
            return "Error: Operator must be '+' or '-'."
        if (len(num1) >= 5 or len(num2) >= 5):
            return "Error: Numbers cannot be more than four digits."

        result_line = ""
        if (symbol == '+'):
            result_line = str(int(num1) + int(num2))
        elif (symbol == '-'):
            result_line = str(int(num1) + int(num2))
        

        length = max(len(num1), len(num2)) + 2
        top_line = num1.rjust(length)
        bottom_line = symbol + str(num2.rjust(length - 1))
        separator_line = "" 
        res = str(result_line).rjust(length)
        for line in range(length):
            separator_line += '-'

        if problem != problems[-1]:
            first += top_line + '    '
            second += bottom_line + '    '
            lines += separator_line + '    '
            sumx += res + '    '
        else:
            first += top_line + '    '
            second += bottom_line + '    '
            lines += separator_line + '    '
            sumx += res + '    '

    if solve:
        string = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        string = first + '\n' + second + '\n' +  lines


    return string


'''
#Call Function
resultado = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print("\n")
print(resultado)
'''