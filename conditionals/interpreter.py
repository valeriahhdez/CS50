'''
This program achieves what the eval() python function does.
It prompts the user for an arithmetic expression. Turn the expression into 
floats and arithmetic operators 
and calculates and outputs the result as a floating-point value formatted to one decimal place
'''

import operator 

# turn string operator into arithmetic operators using the operator module
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
    '%' : operator.mod,
    '^' : operator.xor,
}
# Prompt the user to enter an arithmetic expression
expression = input("Expression: ")

# Function to turn string into floats and arithmetic operators
def eval_expr(op1, oper, op2):
    op1, op2 = float(op1), float(op2)
    return ops[oper](op1, op2)

# Split the string and evaluate the operation
x = eval_expr(*(expression.split()))
print(x)

