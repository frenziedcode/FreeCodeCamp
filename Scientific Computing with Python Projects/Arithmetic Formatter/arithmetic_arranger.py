import re

def arithmetic_arranger(problems) :

    linha1 = ""
    linha2 = ""
    linha2a = ""
    linha3 = ""
    linha4 = ""

    for calc in problems :
        str_calc = str(calc)
        tempNum = re.findall(r'\d+', calc)
        symbol = re.findall(r'[-+*/]', calc)

        intNum0 = int(tempNum[0])
        intNum1 = int(tempNum[1])

        if symbol == ['+']:
            symbol = "+"
            result = intNum0 + intNum1
        elif symbol == ['-']:
            symbol = "-"
            result = intNum0 - intNum1
        else:
            print("Error: Operator must be '+' or '-'")
            exit()

        linha1 += f" {intNum0 : >5} "
        linha2 += f" {symbol : <4}"
        linha2a += f" {intNum1 : >3}"
        linha3 += "----     "
        linha4 += f" {result  : >2}   "

    print(linha1)

#Call Function
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])


