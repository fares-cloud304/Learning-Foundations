# Challenge 14: Multiplication Table (Nested Loops)
# Phase: 2 - Python Programming
# Lesson: 6 - Loops

# Outer loop: Rows (1 to 10)
for i in range(1, 11):
    # Inner loop: Columns (1 to 10)
    for j in range(1, 11):
        # Print the product. end=" " keeps them on the same line
        print(i * j, end=" ")
    # Empty print() moves to the next row after the inner loop finishes
    print()

# CLOUD ENGINEERING CONTEXT:
# Nested loops are used constantly in cloud automation.
# Example 1: Iterating through multiple AWS Regions, then iterating 
# through every EC2 instance inside each region.
# Example 2: Generating IP addresses for VPC Subnets:
# for subnet in range(1, 4):
#     for host in range(1, 255):
#         print(f"10.0.{subnet}.{host}")