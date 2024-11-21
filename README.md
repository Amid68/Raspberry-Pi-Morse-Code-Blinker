# Raspberry Pi Pico Morse Code Blinker

## Description
This project is a "Hello World" for the Raspberry Pi Pico, showcasing the RP2040 microcontroller's **Programmable I/O (PIO)** feature. The onboard or external LED blinks in **Morse code**, spelling "HELLO WORLD". It’s designed to help beginners understand embedded systems programming using the Pico SDK.

## Requirements
- Raspberry Pi Pico.
- C/C++ toolchain and Pico SDK.
- Micro USB cable.
- External LED and resistor (if not using onboard LED).

## Project Structure
```plaintext
src/
├── main.c            # Entry point of the program
├── morse_code.c      # Morse code logic and PIO control
├── morse_code.h      # Header file for Morse code functions
├── morse.pio         # PIO assembly program for LED control
CMakeLists.txt        # Build configuration file for CMake
Makefile              # Simplified build process
README.md             # Project documentation

