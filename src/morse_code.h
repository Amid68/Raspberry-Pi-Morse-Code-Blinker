/************************
 * @file morse_code.h   *
 * @brief               *
 *                      *
 * @author Ameed Othman *
 * @data 2024-11-21     *
 ************************/

#ifndef __MORSE_CODE_H__
#define __MORSE_CODE_H__

#include "pico/stdlib.h"

void init_morse_pio(uint pin);
void send_morse_message(const char * message);

#endif
