# def count_operands_in_expr(expr):
#     c = 0
#     oper = ['*','/','+','-','//','**','%']
#     for i in expr:
#         if isinstance(i,tuple):
#             c+=count_operands_in_expr(i)
#         elif isinstance(i,str):
#             c+=len(i)
#     return c

# print(count_operands_in_expr((3,'**',4)))
# print(count_operands_in_expr(((((2,'+',4),'/',3),'*',2),'+',(3,'**',4))))

# if 1:
#     pass
# else: 
#     raise KeyError("PANIC")
 
def count_operands_in_expr(expr):
    operands = ["+", "-", "*", "/", "%", "**", "//"]
    expr = str(expr)
    if not expr:
        return 0
    else:
        operand = count_operands_in_expr(expr[1:])
        if expr[0] in operands:
            print(f"if {operand +1}")
            return operand + 1
        else:
            print(f"else {operand}")
            return operand

print(count_operands_in_expr(('++',3,'**',4)))
# print(count_operands_in_expr(((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4))))