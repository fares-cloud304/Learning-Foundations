# Challenge 1: String Methods

## What I Did
I solved the first portfolio challenge by manipulating text using string methods. Given the initial string `" Hello World "`, the goal was to clean up the formatting by removing the extra surrounding spaces and converting the entire text to lowercase. 

During my first attempt, I tested the lowercase conversion with:
```python
print("Hewllo world".lower())
# Output: hewllo world
```

After correcting the typo and applying the necessary methods to the target string, I successfully transformed `" Hello World "` into the required `"hello world"` output.

## What I Learned
* **`.lower()` Method:** Converts all uppercase characters in a string into lowercase.
* **`.strip()` Method:** Removes leading and trailing whitespaces, which is essential for cleaning up raw user input or poorly formatted data.
* **Method Chaining:** Learned how to combine multiple string operations together in a single line (like `text.strip().lower()`) to write cleaner, more efficient code.
* **Debugging:** Caught and fixed a syntax typo ("Hewllo") during the testing phase to ensure the final output matched the exact requirements.