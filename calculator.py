

def main():

    inputMessage = input("")

    operandCount = 0
    operand_1 = 0
    operand_2 = 0
    result = ""


    #Считаем количество операторов в строке
    for char in inputMessage:
        if ((char == "+") | (char == "-") | (char == "/") | (char == "*")):
            operandCount += 1



    #Выполняем расчет, разделяя строку оператором и удаляя пробелы
    if operandCount <= 1:

        for i in inputMessage:

            if i == "+":
                textArray = inputMessage.split(i)
                operand_1 = int(textArray[0].strip())
                operand_2 = int(textArray[1].strip())
                if operand_1 & operand_2 <= 10:
                    result = operand_1 + operand_2

            elif i == "-":
                textArray = inputMessage.split(i)
                operand_1 = int(textArray[0].strip())
                operand_2 = int(textArray[1].strip())
                if operand_1 & operand_2 <= 10:
                    result = operand_1 - operand_2

            elif i == "/":
                textArray = inputMessage.split(i)
                operand_1 = int(textArray[0].strip())
                operand_2 = int(textArray[1].strip())
                if operand_1 & operand_2 <= 10:
                    result = operand_1 / operand_2

            elif i == "*":
                textArray = inputMessage.split(i)
                operand_1 = int(textArray[0].strip())
                operand_2 = int(textArray[1].strip())
                if operand_1 & operand_2 <= 10:
                    result = operand_1 * operand_2

    print(result)




main()




