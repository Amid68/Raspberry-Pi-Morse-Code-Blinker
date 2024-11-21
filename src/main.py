"""
********************************************************************************
* @file main.py                                                                *
* @brief Morse Code Blinker for Raspberry Pi Pico                              *
*                                                                              *
* This script blinks an LED on the Raspberry Pi Pico to represent a given      *
* message in Morse code. It uses the onboard LED or an external LED connected  *
* to a specified GPIO pin to blink dots and dashes for each character in the   *
* message.                                                                     *
*                                                                              *
* @author Ameed Othman                                                         *
* @date 2024-11-21                                                             *
*                                                                              *
* @note Timing constants can be adjusted to control the speed of Morse code    *
*       transmission. Use the onboard LED (GPIO 25) or configure the script    *
*       to use an external LED by changing the LED_PIN value.                  *
********************************************************************************
"""

from machine import Pin
import time

"""
********************************************************************************
* Morse Code Dictionary                                                        *
*                                                                              *
* This dictionary maps characters (A-Z, 0-9) to their Morse code equivalents.  *
* Each character is represented as a string of dots (.) and dashes (-).        *
********************************************************************************
"""
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',  ' ': ' '  # Space character
}

"""
********************************************************************************
* Configuration                                                                *
*                                                                              *
* Defines the LED pin and timing constants for Morse code transmission.        *
********************************************************************************
"""
LED_PIN = 25  # Use the onboard LED
led = Pin(LED_PIN, Pin.OUT)

# Timing constants (in seconds)
DOT_TIME = 0.2       # Duration of a dot
DASH_TIME = DOT_TIME * 3  # Duration of a dash
SYMBOL_SPACE = DOT_TIME   # Space between symbols in a character
LETTER_SPACE = DOT_TIME * 3   # Space between letters
WORD_SPACE = DOT_TIME * 7     # Space between words

"""
********************************************************************************
* @brief Blink the LED to represent a Morse code dot.                         *
********************************************************************************
"""
def blink_dot():
    led.on()
    time.sleep(DOT_TIME)
    led.off()
    time.sleep(SYMBOL_SPACE)

"""
********************************************************************************
* @brief Blink the LED to represent a Morse code dash.                        *
********************************************************************************
"""
def blink_dash():
    led.on()
    time.sleep(DASH_TIME)
    led.off()
    time.sleep(SYMBOL_SPACE)

"""
********************************************************************************
* @brief Send a single Morse code character.                                  *
*                                                                              *
* @param char Character to translate into Morse code and blink.               *
********************************************************************************
"""
def send_morse_character(char):
    morse_code = MORSE_CODE_DICT.get(char, '')
    for symbol in morse_code:
        if symbol == '.':
            blink_dot()
        elif symbol == '-':
            blink_dash()
        else:
            # Skip any unknown symbols
            pass
    time.sleep(LETTER_SPACE - SYMBOL_SPACE)

"""
********************************************************************************
* @brief Send a full message in Morse code.                                   *
*                                                                              *
* @param message The message to blink in Morse code.                          *
********************************************************************************
"""
def send_morse_message(message):
    for index, char in enumerate(message.upper()):
        if char == ' ':
            time.sleep(WORD_SPACE - LETTER_SPACE)
        else:
            send_morse_character(char)

"""
********************************************************************************
* @brief Main function to blink the Morse code message in an infinite loop.   *
********************************************************************************
"""
def main():
    message = "HELLO WORLD"
    while True:
        send_morse_message(message)
        time.sleep(2)  # Pause between repetitions

if __name__ == "__main__":
    main()