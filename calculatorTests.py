from calculator import calculate
NO_INPUT_ERROR = "No input was entered."
INVALID_INPUT_ERROR = "Not a valid input"
MISPLACED_OPERATORS = "Misplaced operators"
CONSECUTIVE_OPERATORS_ERROR = "Invalid string, contains consecutive operators"
DIVIDE_BY_ZERO_ERROR = "Cannot divide by zero"
def testCalculate():
    # Test for no string input
    assert calculate("")==NO_INPUT_ERROR

    # Tests for basic computations
    assert calculate("1+2+3+4")==10
    assert calculate("1*2*3*4")==24
    assert calculate("6-5-4-3")==-6
    assert calculate("25/5")==5.0
    assert calculate("30/12")==2.5
    assert calculate("4^2")==16
    assert calculate("exp(4)")==54.598
    assert calculate("log(25)")==3.219
    assert calculate("exp(2+2)")==54.598
    assert calculate("log(5^2)")==3.219

    # Tests for precedence of combined operations
    assert calculate("6*2-7+4")==9
    assert calculate("8+1*1-9")==0
    assert calculate("99-24+9*4")==111
    assert calculate("1+2-4/2")==1
    assert calculate("2^2-4/2")==2
    assert calculate("exp(2+2)")==54.598
    assert calculate("log(5^2)")==3.219

    # Tests for invalid numbers
    assert calculate("x+1")== INVALID_INPUT_ERROR
    assert calculate("p-1")== INVALID_INPUT_ERROR
    assert calculate("a*1")== INVALID_INPUT_ERROR

    # Tests for invalid operations
    assert calculate("1x2")==INVALID_INPUT_ERROR
    assert calculate("1=2")==INVALID_INPUT_ERROR
    assert calculate("log12")==INVALID_INPUT_ERROR

    # Tests for strings beginning and ending with an operation
    assert calculate("1+2+3+")==MISPLACED_OPERATORS
    assert calculate("1+2+3*")==MISPLACED_OPERATORS
    assert calculate("1+2+3-")==MISPLACED_OPERATORS
    assert calculate("1+2+3/")==MISPLACED_OPERATORS
    assert calculate("+1+2+3")==MISPLACED_OPERATORS
    assert calculate("*1+2+3")==MISPLACED_OPERATORS
    assert calculate("--1+2+3")==MISPLACED_OPERATORS
    assert calculate("+-1+2+3")==MISPLACED_OPERATORS
    assert calculate("*-1+2+3")==MISPLACED_OPERATORS
    assert calculate("/1+9")==MISPLACED_OPERATORS
    
    # Tests for negative numbers
    assert calculate("-2+1")==-1
    assert calculate("-2-1")==-3
    assert calculate("-2+-1")==-3
    assert calculate("-2*-2")==4
    assert calculate("2*-2")==-4
    assert calculate("-2*3")==-6
    assert calculate("3--2")==5

    # Tests for consecutive operators
    assert calculate("2+++2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2---2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2**2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2-*2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2+*2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2-+2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2*+2")==CONSECUTIVE_OPERATORS_ERROR

    
    # Test for brackets 
    assert calculate("100/(25-8)")==5.882
    assert calculate("99*2^(exp(3)/log(15))")==16918.690
    # Tests for divison by 0
    assert calculate("5/0")==DIVIDE_BY_ZERO_ERROR
    assert calculate("12/(10-10)")==DIVIDE_BY_ZERO_ERROR
