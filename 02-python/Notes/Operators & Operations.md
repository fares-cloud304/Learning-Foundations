# Python Fundamentals: Operators & Operations

A collection of reference notes covering Python operators, their applications in security, networking, and core programming logic.

---

## 1. Bitwise Operators
Bitwise operators manipulate data at the lowest level—individual binary bits (`0` and `1`). They are highly critical in network engineering, cryptography, and systems security.

*   `&` (AND)
*   `|` (OR)
*   `^` (XOR)
*   `~` (NOT)
*   `<<` (Left Shift)
*   `>>` (Right Shift)

### Real-World Applications
*   **IP Subnet Masking (AND):** Used to determine network addresses. 
    *   *Example:* `192.168.1.100 & 255.255.255.0 = 192.168.1.0`
*   **Encryption (XOR):** Fundamental building block in symmetric cryptography algorithms.
*   **File Permissions (Bit Masks):** Linux file systems map numbers to permission flags. 
    *   *Example:* `755` translates directly to the binary flag layout `rwxr-xr-x`.

### Execution Example
*   `12 & 10 = 8`
    *   Binary of 12: `1100`
    *   Binary of 10: `1010`
    *   Result (`1100 & 1010`): `1000` (which is `8` in decimal)

---

## 2. Comparison & Logical Operators
These operators evaluate expressions and return Boolean values (`True` or `False`). They drive conditional decision-making structures (`if/else`).

### Comparison Operators
Used to compare two distinct values:
*   `==` (Equal to)
*   `!=` (Not equal to)
*   `<` (Less than)
*   `>` (Greater than)
*   `<=` (Less than or equal to)
*   `>=` (Greater than or equal to)

### Logical Operators
Used to combine multiple conditional statements:
*   `and` (Returns True only if **both** sides are True)
*   `or` (Returns True if **at least one** side is True)
*   `not` (Reverses the Boolean value)

### Core Rules & Precedence
*   **Boolean Checking:** `has_id == True` explicitly validates if both conditions align.
*   **Security Context:** `if port == 22 and is_open:` triggers an alert only when a vulnerable port is completely accessible.
*   **Operator Precedence:** Mathematical logic applies here. For example, `2 + 3 * 4 = 14` (not `20`) because multiplication is always evaluated first.

---

## 3. Arithmetic Operators
Python supports standard mathematical computations alongside specialized division styles.

*   `+` (Addition)
*   `-` (Subtraction)
*   `*` (Multiplication)
*   `/` (Division — **always returns a float**, e.g., `4 / 2 = 2.0`)
*   `//` (Floor Division — cuts off the decimal entirely and rounds down)
*   `%` (Modulo — extracts only the remainder of a division)
*   `**` (Exponent/Power)

### Real-World Applications
*   **Modulo (`%`) in Security:** Used heavily in hashing functions and key generation algorithms like RSA encryption.
    *   *Example:* `17 % 5 = 2` (17 divided by 5 leaves a remainder of 2).
*   **Floor Division (`//`):** Essential for cleanly implementing pagination (e.g., calculation of page counts) and batch processing scripts.
Use code with caution.