#####################################################
# @file CMakeLists.txt                              #
# @brief CMake configuration for Morse Code project #
#                                                   #
# @author Ameed Othman                              #
# @date 2024-11-21                                  #
#####################################################

cmake_minimum_required(VERSION 3.13)

# Set the absolute path to the Pico SDK
set(PICO_SDK_PATH "/Users/amid/dev/embedded/raspberry_pi/pico-sdk")

# Include the Pico SDK (must be before project())
include("${PICO_SDK_PATH}/external/pico_sdk_import.cmake")

# Set project name
project(morse_code_project)

# Initialize the Pico SDK
pico_sdk_init()

# Add the executable target
add_executable(morse_code
    src/main.c
    src/morse_code.c
)

# Generate PIO header
pico_generate_pio_header(morse_code "${CMAKE_CURRENT_LIST_DIR}/src/morse.pio")

# Link the libraries
target_link_libraries(morse_code pico_stdlib hardware_pio)

# Enable stdio via USB, disable UART
pico_enable_stdio_usb(morse_code 1)
pico_enable_stdio_uart(morse_code 0)

# Create map/bin/hex/uf2 files
pico_add_extra_outputs(morse_code)
