# How a Computer Works: Boot Process

## CPU
Central Processing Unit.
The CPU executes instructions it receives from RAM.

## RAM
Random Access Memory.
Temporary high-speed storage used while programs are running.

## BIOS / UEFI
Firmware stored on the motherboard that starts when the computer powers on.

## POST
Power On Self Test.
Checks if hardware components are working correctly.

## Boot Process

1. Power button is pressed
2. Electricity reaches the motherboard
3. BIOS/UEFI starts
4. POST checks hardware
5. Bootloader starts
6. Operating System loads
7. Programs can run

## Commands Learned

### Linux

`journalctl -b`

Shows logs from the current boot.
Useful for investigating system problems.