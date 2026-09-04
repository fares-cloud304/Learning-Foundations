# Challenge 10: Decimal to Binary using Bitwise Operators
# Phase: 2 - Python Programming
# Lesson: 4 - Control Flow & Logic

def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary_string = ""
    
    while n > 0:
        # & 1 checks the rightmost bit (0 or 1)
        bit = n & 1
        
        # Prepend the bit to our result string
        binary_string = str(bit) + binary_string
        
        # >> 1 shifts bits right (equivalent to integer division by 2)
        n = n >> 1
        
    return binary_string

# Interactive test
number = int(input("Enter a decimal number: "))
print(f"Binary of {number} is: {decimal_to_binary(number)}")

# CLOUD ENGINEERING CONTEXT:
# Bitwise operators are extremely fast because they bypass normal math 
# and talk directly to the CPU's memory bits. In cloud security, 
# bitwise operations are used to calculate Subnet Masks (CIDR blocks) 
# and network IP ranges at high speed.