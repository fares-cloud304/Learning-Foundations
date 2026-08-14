# Binary, Hexadecimal, and Data Representation

## Bits and Bytes

- 8 bits = 1 byte.
- Computers represent data using binary (0s and 1s).

## Binary

- Binary uses only 0 and 1.
- Each position represents a power of 2.
- Binary can be converted to decimal by adding the powers of 2 where the bit is 1.

## Hexadecimal

- Hexadecimal uses 16 symbols:
  - 0–9
  - A–F
- A = 10, B = 11, ..., F = 15.
- Hexadecimal is a compact way of representing binary data.

## Decimal and Binary Conversion

- Decimal numbers can be converted to binary.
- Binary numbers can be converted to decimal using powers of 2.

## ASCII

- ASCII stands for American Standard Code for Information Interchange.
- It represents characters using numeric values.
- ASCII covers 128 characters.

## Hashing

- SHA-256 creates a hash from data.
- A hash can be used to verify file integrity.
- A changed file should produce a different hash.

## Hex / File Inspection

- Hexdump can display file contents in hexadecimal.
- File formats can have identifying bytes at the beginning.
- These are called magic bytes.

## Commands I Used

```bash
sha256sum "filename"
hexdump -C "filename"s