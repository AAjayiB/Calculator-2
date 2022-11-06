import re, math

ERROR_MESSAGES = ["No input was entered.", "Not a valid input", "Expression cannot begin with an operation",
                  "Expression cannot end with an operation", "Invalid string, contains consecutive operators",
                  "Expression has mismatched brackets"]
l = "log"


def calculate(exp):
    answer = (0, "")

    if exp:
        if re.search(r"[$&]", exp):
            return -1, ERROR_MESSAGES[1]
        exp = exp.replace("log(", "$(")
        exp = exp.replace("exp(", "&(")
        # checks for any non operators or digits
        if not re.search(r"[^\d+\-\*\(\)/\$\&\.]", exp):
            # checks for expressions beginning only with a single minus or not
            if re.search(r"^\-?\d|\(", exp):
                # checks for expressions ending with only digits
                if re.search(r"\d|\)$", exp):
                    ############# ACTUAL OPERATIONS #############
                    validExpression = re.findall(r"\d+\.?\d*|[+\-\*\(\)/\$\&]", exp)
                    ############# Here at the moment
                    if validExpression[0] == "-":
                        validExpression[0:2] = ["".join(validExpression[0:2])]

                    while (validExpression.count("(") > 0):
                        opIndex = validExpression.index("(")
                        counter = 1
                        otherCounter = 1
                        inBrackets = ""
                        for i in validExpression[opIndex + 1:]:
                            otherCounter += 1
                            if i == '(':
                                counter += 1
                            if i == ')':
                                counter -= 1
                            if counter == 0:
                                result = calculate(inBrackets)
                                if result[1] != "":
                                    return result
                                break
                            inBrackets = inBrackets + i
                        if counter != 0:
                            return [-1, ERROR_MESSAGES[5]]
                        for i in range(otherCounter):
                            validExpression.pop(opIndex)
                        validExpression.insert(opIndex, result[0])

                    while (validExpression.count("$") > 0):
                        opIndex = validExpression.index("$")
                        computedValue = math.log(float(validExpression[opIndex+1]))
                        validExpression.pop(opIndex)
                        validExpression[opIndex] = computedValue

                    while (validExpression.count("*") > 0):
                        opIndex = validExpression.index("*")
                        if validExpression[opIndex - 1] == "+" or validExpression[opIndex - 1] == "-":
                            return -1, ERROR_MESSAGES[4]
                        if (validExpression[opIndex + 1] == "+" or validExpression[opIndex + 1] == "*"):
                            return -1, ERROR_MESSAGES[4]
                        if (validExpression[opIndex + 1] == "+" or validExpression[opIndex + 1] == "*") and (
                                validExpression[opIndex + 2] == "+" or validExpression[opIndex + 2] == "-" or
                                validExpression[opIndex + 2] == "*"):
                            return -1, ERROR_MESSAGES[4]
                        if validExpression[opIndex + 1] == "-" and (
                                validExpression[opIndex + 2] == "+" or validExpression[opIndex + 2] == "-" or
                                validExpression[opIndex + 2] == "*"):
                            return -1, ERROR_MESSAGES[4]
                        if validExpression[opIndex + 1] == "-":
                            validExpression[opIndex + 1:opIndex + 3] = [
                                "".join(validExpression[opIndex + 1:opIndex + 3])]
                        computedValue = float(validExpression[opIndex - 1]) * float(validExpression[opIndex + 1])
                        validExpression[opIndex - 1] = computedValue
                        validExpression.pop(opIndex + 1)
                        validExpression.pop(opIndex)

                    while (validExpression.count("-") > 0):
                        opIndex = validExpression.index("-")
                        print(validExpression)
                        if validExpression[opIndex + 1] == "+":
                            return -1, ERROR_MESSAGES[4]
                        if validExpression[opIndex + 1] == "-" and (
                                validExpression[opIndex + 2] == "-" or validExpression[opIndex + 2] == "+"):
                            return -1, ERROR_MESSAGES[4]
                        else:
                            validExpression[opIndex:opIndex + 2] = "+"
                            print(validExpression)
                        if validExpression[opIndex] == "-":
                            computedValue = float(validExpression[opIndex - 1]) - float(validExpression[opIndex + 1])
                            validExpression[opIndex - 1] = computedValue
                            validExpression.pop(opIndex + 1)
                            validExpression.pop(opIndex)

                    while (validExpression.count("+") > 0):
                        opIndex = validExpression.index("+")
                        if validExpression[opIndex + 1] == "+":
                            return -1, ERROR_MESSAGES[4]
                        computedValue = float(validExpression[opIndex - 1]) + float(validExpression[opIndex + 1])
                        validExpression[opIndex - 1] = computedValue
                        validExpression.pop(opIndex + 1)
                        validExpression.pop(opIndex)

                    answer = (validExpression[0], "")

                else:
                    answer = (-1, ERROR_MESSAGES[3])
            else:
                answer = (-1, ERROR_MESSAGES[2])
        else:
            answer = (-1, ERROR_MESSAGES[1])
    else:
        answer = (-1, ERROR_MESSAGES[0])
    return answer


def Main():
    print("Enter an expression")
    result = calculate((input()))
    if result[1] == "":
        print(result[0])
    else:
        print(result[1])
    # r=re.search(r"log","shsudflogfjswi")
    # if r():
    #     print("is there")
    # else:


if __name__ == "__main__":
    Main()
