# Challenge: PNG Magic Bytes

## Task
Use hexdump to inspect a PNG and identify its magic bytes.

## Command
hexdump -C "filename.png" | head

## PNG Signature
89 50 4E 47 0D 0A 1A 0A

## What I learned
Files can contain characteristic bytes at the beginning that help identify their format.
PNG files begin with a specific signature called their magic bytes.