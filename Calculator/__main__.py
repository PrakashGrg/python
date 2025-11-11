from Jeff import add_numbers
from sam import subtract_numbers
from Asu import multiply_numbers
from pu import division_numbers

input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))
input3 = input("Enter operation (+ or - or * or /): ")

if __name__ == "__main__":  # Corrected from "_main_" to "__main__"
    if input3 == "+":
        sum_result = add_numbers(input1, input2)
        print("The sum is:", sum_result)
    elif input3 == "-":
        diff_result = subtract_numbers(input1, input2)
        print("The difference is:", diff_result)
    elif input3 == "*":
        multi_result = multiply_numbers(input1, input2)
        print("The multiplication of:", multi_result)
    elif input3 == "/":
        div_result = division_numbers(input1, input2)
        print("The division is:", div_result)
    else:
        print("Invalid operation. Please enter + or - or *.")