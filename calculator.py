import re

CONSECUTIVE_OPERATORS ="Invalid string, contains consecutive operators"
l = "log"
def calculate(exp):
    answer=""

    if exp:
        # checks for any non operators or digits
        if not re.search(r"[^\d\+\-\*\/\^]",exp):
            # checks for expressions beginning only with a single minus or not
            if re.search(r"^\-?\d",exp):
                # checks for expressions ending with only digits 
                if re.search(r"\d$", exp):
                    ############# ACTUAL OPERATIONS #############
                    validExpression = re.findall(r"\d+|[\+\-\*\/\^]", exp)
                    ############# Here at the moment
                    if validExpression[0] =="-":
                        validExpression[0:2]=["".join(validExpression[0:2])]

                    while (validExpression.count("^") > 0):
                        opIndex = validExpression.index("^")
                        if validExpression[opIndex-1]=="+" or validExpression[opIndex-1]=="-" or validExpression[opIndex-1]=="/" or validExpression[opIndex-1]=="^": 
	                        return CONSECUTIVE_OPERATORS
                        if (validExpression[opIndex+1]=="+" or validExpression[opIndex+1]=="*" or validExpression[opIndex+1]=="/" or validExpression[opIndex+1]=="^"):
                            return CONSECUTIVE_OPERATORS
                        if (validExpression[opIndex+1]=="+" or validExpression[opIndex+1]=="*") and (validExpression[opIndex+2]=="+" or validExpression[opIndex+2]=="-" or validExpression[opIndex+2]=="*" or validExpression[opIndex+2]=="/" or validExpression[opIndex+2]=="^"): 
	                        return CONSECUTIVE_OPERATORS
                        if validExpression[opIndex+1] =="-" and (validExpression[opIndex+2]=="+" or validExpression[opIndex+2]=="-" or validExpression[opIndex+2]=="*" or validExpression[opIndex+2]=="/" or validExpression[opIndex+2]=="^"): 
	                        return CONSECUTIVE_OPERATORS
                        if validExpression[opIndex+1] =="-":
                            validExpression[opIndex+1:opIndex+3] = ["".join(validExpression[opIndex+1:opIndex+3])]
                        computedValue = int(validExpression[opIndex-1])**int(validExpression[opIndex+1])
                        validExpression[opIndex-1] = computedValue
                        validExpression.pop(opIndex+1)
                        validExpression.pop(opIndex)

                    while (validExpression.count("/") > 0):
                        opIndex = validExpression.index("/")
                        if validExpression[opIndex-1]=="+" or validExpression[opIndex-1]=="-" or validExpression[opIndex-1]=="/": 
	                        return CONSECUTIVE_OPERATORS
                        if (validExpression[opIndex+1]=="+" or validExpression[opIndex+1]=="*" or validExpression[opIndex+1]=="/"):
                            return CONSECUTIVE_OPERATORS
                        if (validExpression[opIndex+1]=="+" or validExpression[opIndex+1]=="*") and (validExpression[opIndex+2]=="+" or validExpression[opIndex+2]=="-" or validExpression[opIndex+2]=="*" or validExpression[opIndex+2]=="/"): 
	                        return CONSECUTIVE_OPERATORS
                        if validExpression[opIndex+1] =="-" and (validExpression[opIndex+2]=="+" or validExpression[opIndex+2]=="-" or validExpression[opIndex+2]=="*" or validExpression[opIndex+2]=="/"): 
	                        return CONSECUTIVE_OPERATORS
                        if validExpression[opIndex+1] =="-":
                            validExpression[opIndex+1:opIndex+3] = ["".join(validExpression[opIndex+1:opIndex+3])]
                        computedValue = int(validExpression[opIndex-1])/int(validExpression[opIndex+1])
                        validExpression[opIndex-1] = computedValue
                        validExpression.pop(opIndex+1)
                        validExpression.pop(opIndex)

                    while (validExpression.count("*") > 0):
                        opIndex = validExpression.index("*")
                        if validExpression[opIndex-1]=="+" or validExpression[opIndex-1]=="-": 
	                        return CONSECUTIVE_OPERATORS
                        if (validExpression[opIndex+1]=="+" or validExpression[opIndex+1]=="*"):
                            return CONSECUTIVE_OPERATORS
                        if (validExpression[opIndex+1]=="+" or validExpression[opIndex+1]=="*") and (validExpression[opIndex+2]=="+" or validExpression[opIndex+2]=="-" or validExpression[opIndex+2]=="*"): 
	                        return CONSECUTIVE_OPERATORS
                        if validExpression[opIndex+1] =="-" and (validExpression[opIndex+2]=="+" or validExpression[opIndex+2]=="-" or validExpression[opIndex+2]=="*"): 
	                        return CONSECUTIVE_OPERATORS
                        if validExpression[opIndex+1] =="-":
                            validExpression[opIndex+1:opIndex+3] = ["".join(validExpression[opIndex+1:opIndex+3])]
                        computedValue = int(validExpression[opIndex-1])*int(validExpression[opIndex+1])
                        validExpression[opIndex-1] = computedValue
                        validExpression.pop(opIndex+1)
                        validExpression.pop(opIndex)

                    while (validExpression.count("-") > 0):
                        opIndex = validExpression.index("-")
                        print(validExpression)
                        if validExpression[opIndex+1]=="+":
                            return CONSECUTIVE_OPERATORS
                        if validExpression[opIndex+1]=="-" and (validExpression[opIndex+2]=="-" or validExpression[opIndex+2]=="+"):
                            return CONSECUTIVE_OPERATORS
                        elif validExpression[opIndex-1]=="+" and (validExpression[opIndex-2]=="-" or validExpression[opIndex-2]=="+"):
                            CONSECUTIVE_OPERATORS
                        elif validExpression[opIndex-1]=="+":
                            validExpression[opIndex-1:opIndex+1]="-"
                        elif validExpression[opIndex+1]=="-":
                            validExpression[opIndex:opIndex+2]="+"
                            print(validExpression)
                         
                        if validExpression[opIndex]=="-":
                            computedValue = int(validExpression[opIndex-1])-int(validExpression[opIndex+1])
                            validExpression[opIndex-1] = computedValue
                            validExpression.pop(opIndex+1)
                            validExpression.pop(opIndex)
                        
                    
                    while (validExpression.count("+") > 0):
                        opIndex = validExpression.index("+")
                        if validExpression[opIndex+1]=="+":
                            return CONSECUTIVE_OPERATORS
                        computedValue = int(validExpression[opIndex-1])+int(validExpression[opIndex+1])
                        validExpression[opIndex-1] = computedValue
                        validExpression.pop(opIndex+1)
                        validExpression.pop(opIndex)

                    answer=str(validExpression[0])

                else:
                    answer="Expression cannot end with an operation"
            else:
                answer="Expression cannot begin with an operation"
        else:
            answer="Not a valid input"
    else:
        answer="No input was entered."
    return answer

def Main():
    while (1):
        print("Enter an expression")
        print(calculate(input()))
    # r=re.search(r"log","shsudflogfjswi")
    # if r():
    #     print("is there")
    # else:


if __name__=="__main__":
    Main()