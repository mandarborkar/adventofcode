
def calculate_value (operation):

    operation_index = [i for i in range(len(operation)) if operation.startswith('+', i)] + [i for i in range(len(operation)) if operation.startswith('*', i)]
    operation_index.sort ()

    value = int(operation[:operation_index[0]])

    for i in range (0, len(operation_index)):
        operator = operation[operation_index[i]]
        if i+1 < len(operation_index) :
            operand = operation[operation_index[i]+1:operation_index[i+1]]
        else:
            operand = operation[operation_index[i]+1:]

        if operator == '+':
            value = value + int(operand)
        elif operator == '*':
            value = value * int(operand)

    return value

def process_parathesis (expression):

    paranthesis_start = [i for i in range(len(expression)) if expression.startswith('(', i)]
    print (paranthesis_start)

    if paranthesis_start == [] :
        final_calculation = calculate_value(expression)
        print ('final ' + expression + ' = ' + str(final_calculation))
        return final_calculation

    paranthesis_end = [i for i in range(len(expression)) if expression.startswith(')', i)]
    print (paranthesis_end)
    j=0
    while  paranthesis_end[0] > paranthesis_start[j] and j+1 < len(paranthesis_start):
        j = j + 1
    print ('interim ' + expression[paranthesis_start[j-1]+1:paranthesis_end[0]])
    interim_value = calculate_value(expression[paranthesis_start[j-1]+1:paranthesis_end[0]])
    print ('interim ' + expression[paranthesis_start[j-1]+1:paranthesis_end[0]] + ' = ' + str(interim_value))
    interim_value = process_parathesis(expression[0:paranthesis_start[j-1]]+
               str(interim_value)
               +expression[paranthesis_end[0]+1:])
    return interim_value

# Main program

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent18input.txt", "r")
operation = f1.readlines()

final_calculation = 0

for i in range (0,len(operation)):
    operation[i] = operation[i].replace ('\n','')
    operation[i] = operation[i].replace (' ','')
#    operation[i] = operation[i].replace ('(','')
#    operation[i] = operation[i].replace(')', '')

print (operation[1])
final_calculation += process_parathesis (operation[1])

print ('finalvalue ' + operation[1] + ' = ' + str(final_calculation))