/*************************
 * @file main.c
 * @brief
 *
 * @author Ameed Othman
 * @date 2024-11-21
 *************************/
#include "pico/stdlib.h"
#include "morse_code.h"
#include "morse.pio.h"

int main() {
    ustdio_init_all();
    printf("Program started\n");
    int led_pin = PICO_DEFAULT_LED_PIN;
    init_morse_pio(led_pin);

    const char * message = "HELLO WORLD";
    while (true) {
        send_morse_message(message);
        sleep_ms(2000);
    }
    
    return 0;
}