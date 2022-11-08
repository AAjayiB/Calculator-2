from calculator import calculate
NO_INPUT_ERROR = "No input was entered."
INVALID_INPUT_ERROR = "Not a valid input"
OPERATION_END_ERROR = "Expression cannot end with an operation"
OPERATION_BEGIN_ERROR = "Expression cannot begin with an operation"
CONSECUTIVE_OPERATORS_ERROR = "Invalid string, contains consecutive operators"
def testCalculate():
    # Test for no string input
    assert calculate("")==NO_INPUT_ERROR

    # Tests for basic computations
    assert calculate("1+2+3+4")=="10"
    assert calculate("1*2*3*4")=="24"
    assert calculate("6-5-4-3")=="-6"
    assert calculate("25/5")=="5.0"
    assert calculate("30/12")=="2.5"
    assert calculate("4^2")=="16"


    # Tests for precedence of combined operations
    assert calculate("6*2-7+4")=="9"
    assert calculate("8+1*1-9")=="0"
    assert calculate("99-24+9*4")=="111"
    assert calculate("1+2-4/2")=="1"
    assert calculate("2^2-4/2")=="2"
   

    # Tests for invalid numbers
    assert calculate("x+1")== INVALID_INPUT_ERROR
    assert calculate("p-1")== INVALID_INPUT_ERROR
    assert calculate("a*1")== INVALID_INPUT_ERROR

    # Tests for invalid operations
    assert calculate("1x2")==INVALID_INPUT_ERROR
    assert calculate("1=2")==INVALID_INPUT_ERROR
    assert calculate("log12")==INVALID_INPUT_ERROR

    # Tests for strings beginning and ending with an operation
    assert calculate("1+2+3+")==OPERATION_END_ERROR
    assert calculate("1+2+3*")==OPERATION_END_ERROR
    assert calculate("1+2+3-")==OPERATION_END_ERROR
    assert calculate("1+2+3/")==OPERATION_END_ERROR
    assert calculate("+1+2+3")==OPERATION_BEGIN_ERROR
    assert calculate("*1+2+3")==OPERATION_BEGIN_ERROR
    assert calculate("--1+2+3")==OPERATION_BEGIN_ERROR
    assert calculate("+-1+2+3")==OPERATION_BEGIN_ERROR
    assert calculate("*-1+2+3")==OPERATION_BEGIN_ERROR
    assert calculate("/1+9")==OPERATION_BEGIN_ERROR
    
    # Tests for negative numbers
    assert calculate("-2+1")=="-1"
    assert calculate("-2-1")=="-3"
    assert calculate("-2+-1")=="-3"
    assert calculate("-2*-2")=="4"
    assert calculate("2*-2")=="-4"
    assert calculate("-2*3")=="-6"
    assert calculate("3--2")=="5"

    # Tests for consecutive operators
    assert calculate("2+++2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2---2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2**2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2-*2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2+*2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2-+2")==CONSECUTIVE_OPERATORS_ERROR
    assert calculate("2*+2")==CONSECUTIVE_OPERATORS_ERROR


