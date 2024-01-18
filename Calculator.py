"Importing math module for trigonometric functions."
import math

"Defining function for register."
def register(input_bits, load, output_bits):
    if load:
        output_bits = [input_bits].copy()
    return output_bits

"Defining function for decimal to binary conversion."
def decimal_to_binary(decimal):
    binary = []
    for i in range(16):
        binary.append(decimal % 2)
        decimal = decimal // 2
    return binary[::-1]

"Defining function for binary to decimal conversion."
def binary_to_decimal(binary_list):
    decimal = 0
    for i, bit in enumerate(binary_list):
        decimal += bit * (2 ** (15 - i))
    return decimal

"Defining function for mux16."
def mux16(a, b, sel):
    if sel == 0:
        return a
    else:
        return b

"Defining function for not16."
def not16(a):
    return [not i for i in a]

"Defining function for and16."
def and16(a, b):
    return [i and j for i, j in zip(a, b)]

"Defining function for or gate."
def or_gate(a, b):
    return [a[0] | b[0]]

"Defining function for or8way."
def or8way(a):
    return any(a)

"Defining function for add 16)"
def add16(a, b):
    result = [0] * 16
    carry = 0
    for i in range(15, -1, -1):
        sum = a[i] + b[i] + carry
        carry = sum // 2
        result[i] = sum % 2
    return result

"Defining ALU function using the previous combinational circuit functions."
def ALU(a, b, zx, nx, zy, ny, f, no):
    a = mux16(a, [0]*16, zx)
    a = mux16(a, not16(a), nx)
    b = mux16(b, [0]*16, zy)
    b = mux16(b, not16(b), ny)
    if f == 0:
        out = and16(a, b)
    else:
        out = add16(a, b)
    out = mux16(out, not16(out), no)
    return out

"Declaring variables to store answers."
Register1 = []
Register2 = []
Register3 = []
Register4 = []
Register5 = []
list_result = []

while True:
    "Obtaining number of inputs."
    input_num = int(input("Enter number of inputs: "))
    
    if input_num == 1:
        num1 = input("Enter a number: ")

        "To use the previous answers."
        if num1 == 'ans':
            num = int(input("Enter which answer you require: "))
            num1 = list_result[num]
        else:
            num1 = int(num1)
            
        op = input("Possible operations are all trigonometric and exponential functions. Select one: ")
        
        if op == 'sin':
            result = math.sin(int(num1))
        elif op == 'cos':
            result = math.cos(int(num1))
        elif op == 'tan':
            result = math.tan(int(num1))
        elif op == 'e':
            result = math.exp(int(num1))
        elif op == 'ln':
            result = math.log(int(num1))
        else:
            print("The operator is incorrect. Please try again.")
            continue
        
    elif input_num == 0:
        print("The number of inputs is invalid. Please try again.")

    else:
        numbers = [] 
        bin_numbers = []
        for i in range(input_num):
            element = input("Enter a number: ")
            if element != 'ans':
                numbers.append(int(element))
            else:
                num = int(input("Enter which answer you require: "))
                element = list_result[num]
                element = element[0]
                numbers.append(element)
            
        op = input("Enter a operator: ")
        
        for i in range(input_num):
            bin_numbers.append(decimal_to_binary(numbers[i]))
            
        if op == '+':
            out1 = ALU(bin_numbers[0], bin_numbers[1], 0, 0, 0, 0, 1, 0)
            result = binary_to_decimal(out1)
            for i in range(2,input_num):
                out1 = ALU(out1, bin_numbers[i], 0, 0, 0, 0, 1, 0)
                out2 = binary_to_decimal(out1)
                result = out2

        elif op == '-':
            out1 = ALU(bin_numbers[0], bin_numbers[1], 0, 1, 0, 0, 1, 1)
            result = binary_to_decimal(out1)
            for i in range(2,input_num):
                out1 = ALU(out1, bin_numbers[i], 0, 1, 0, 0, 1, 1)
                out2 = binary_to_decimal(out1)
                result = out2

        elif op == '&':
            out1 = ALU(bin_numbers[0], bin_numbers[1], 0, 0, 0, 0, 0, 0)
            result = binary_to_decimal(out1)
            for i in range(2,input_num):
                out1 = ALU(out1, bin_numbers[i], 0, 0, 0, 0, 0, 0)
                out2 = binary_to_decimal(out1)
                result = out2

        elif op == '|':
            out1 = ALU(bin_numbers[0], bin_numbers[1], 0, 1, 0, 1, 0, 1)
            result = binary_to_decimal(out1)
            for i in range(2,input_num):
                out1 = ALU(out1, bin_numbers[i], 0, 1, 0, 1, 0, 1)
                out2 = binary_to_decimal(out1)
                result = out2

        elif op == '!':
            out1 = ALU(bin_numbers[0], bin_numbers[1], 0, 0, 1, 1, 0, 1)
            result = binary_to_decimal(out1)
            for i in range(2,input_num):
                out1 = ALU(out1, bin_numbers[i], 0, 0, 1, 1, 0, 1)
                out2 = binary_to_decimal(out1)
                result = out2

        elif op == '*':
            out1 = numbers[0] * numbers[1]
            result = out1
            for i in range(2,input_num):
                out1 = out1 * numbers[i]
                result = out1

        elif op == '/':
            out1 = numbers[0] / numbers[1]
            result = out1
            for i in range(2,input_num):
                out1 = out1 / numbers[i]
                result = out1
                
        elif op == '^':
            out1 = numbers[0] ** numbers[1]
            result = out1
            for i in range(2,input_num):
                out1 = out1 ** numbers[i]
                result = out1

        else:
            print("The operator is invalid. Please try again.")
            continue

    print("The answer is : ", result)
    Register5 = Register4
    Register4 = Register3
    Register3 = Register2
    Register2 = Register1
    Register1 = register(result, 1, Register1)
    list_result = [Register1, Register2, Register3, Register4, Register5]
    choice = input("Would you like to continue? (Enter Y/N) : ")
    if choice == 'Y':
        continue
    else:
        print("Thank you for using the calculator.")
        break
