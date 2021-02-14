
def find_operation (operation):
    i=0
    j=0
    int_op = []
    print (operation)
    print (len(operation))
    while j < len (operation) :
        j = j+1
        if operation[j] == ')':
            print('found op2=' + str(len(operation[1:j])) + ' ' + operation[1:j])
            return operation[1:j]
        elif operation[j] == '(':
            int_op=find_operation(operation[j:])
            j = j +2+ len(int_op)
        print (str(j) + ' ' + operation[j:])

def calculate_value (operation):
    value = int(operation[0])
    for i in range (1, len(operation), 2):
        if operation[i] == '+':
            value = value + int(operation[i + 1])
        elif operation[i] == '*':
            value = value * int(operation[i + 1])
    return value

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent18input.txt", "r")
operation = f1.readlines()

for i in range (0,len(operation)):
    operation[i] = operation[i].replace ('\n','')
    operation[i] = operation[i].replace (' ','')
#    operation[i] = operation[i].replace ('(','')
#    operation[i] = operation[i].replace(')', '')
print (operation[0])

print('found op3=' + find_operation(operation[0][2:]))
#final_value = calculate_value(operation[0])
# print ( operation[0] + ' = ' + str(final_value))