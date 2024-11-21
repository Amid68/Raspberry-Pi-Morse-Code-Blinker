# File: Makefile

# Project variables
PROJECT_NAME = morse_code
BUILD_DIR = build

# Path to the Pico SDK (adjust this if necessary)
PICO_SDK_PATH = ../../pico-sdk

# Default target
all: build
# Path to the Pico SDK
PICO_SDK_PATH = /Users/amid/dev/embedded/raspberry_pi/pico-sdk

build:
	mkdir -p build
	cd build && cmake .. -DPICO_SDK_PATH=$(PICO_SDK_PATH)
	cd build && make

# Clean the build directory
clean:
	rm -rf $(BUILD_DIR)

# Flash the compiled binary to the Pico
flash: build
	cp $(BUILD_DIR)/$(PROJECT_NAME).uf2 /Volumes/RPI-RP2/
