# Challenge 25: File Reader
# Phase: 2 - Python Programming
# Lesson: 10 - File I/O & Error Handling

# Use the context manager (with) to safely open the file
with open("test_log.txt", "r") as f:
    content = f.read()

# Count Lines (Split by newline character)
lines = content.split("\n")
line_count = len(lines)

# Count Words (Split by space)
words = content.split(" ")
word_count = len(words)

# Count Characters (Just the length of the whole string)
char_count = len(content)

# Print the report
print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")

# CLOUD ENGINEERING CONTEXT:
# Counting lines and words in log files is a daily task for cloud engineers.
# Example: If an AWS CloudTrail log has 50,000 lines, you know 50,000 API 
# calls occurred. This helps estimate the scale of an attack or 
# calculate billing for log processing services like AWS Athena.