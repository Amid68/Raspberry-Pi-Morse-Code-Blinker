/**************************
 * @file mourse_code.c
 * @brief
 * 
 * @author Ameed Othman
 * @data 2024-11-21
 *************************/

#include "morse_code.h"
#include "hardware/pio.h"
#include "hardware/clocks.h"
#include "morse.pio.h"

static const char * morse_table[36] = {
    ".-", "-...", "-.-.", "-..", ".",               // A-E
    "..-.", "--.", "....", "..", ".---",            // F-J
    "-.-", ".-..", "--", "-.", "---",               // K-O
    ".--.", "--.-", ".-.", "...", "-",              // P-T
    "..-", "...-", ".--", "-..-", "-.--", "--..",   // U-Z
    "-----", ".----", "..---", "...--", "....-",    // 0-4
    ".....", "-....", "--...", "---..", "----."     // 5-9
};

void init_morse_pio(uint pin) {
    PIO pio = pio0;
    uint offset = pio_add_program(pio, &morse_program);
    uint sm = pio_claim_unused_sm(pio, true);

    // Set the pin for the state machine
    pio_sm_set_consecutive_pindirs(pio, sm, pin, 1, true); // Set the pin as output

    // Configure the state machine
    pio_sm_config c = morse_program_get_default_config(offset);
    sm_config_set_sideset_pins(&c, pin); // Configure side-set pin
    sm_config_set_set_pins(&c, pin, 1);  // Configure set pin

    pio_sm_init(pio, sm, offset, &c);
    pio_sm_set_enabled(pio, sm, true);
}

void send_morse_character(PIO pio, uint sm, char c) {
    const char * morse_code;
    if (c >= 'A' && c <= 'Z') {
        morse_code = morse_table[c - 'A'];
    } else if (c >= '0' && c <= '9') {
        morse_code = morse_table[c - '0' + 26];
    } else if (c == ' ') {
        sleep_ms(700);
        return;
    } else {
        return;
    }

    while (*morse_code) {
        uint32_t symbol_length = (*morse_code == '.') ? 1 : 3;
        pio_sm_put_blocking(pio, sm, symbol_length);
        sleep_ms(200);
        morse_code++;
    }
    sleep_ms(500);
}

void send_morse_message(const char * message) {
    PIO pio = pio0;
    uint sm = 0;
    while (*message) {
        char c = toupper((unsigned char)*message);
        send_morse_character(pio, sm, c);
        message++;
    }
}

