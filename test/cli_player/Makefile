CC = gcc

SRC_DIR =../../src
SAECLIB_DIR =$(SRC_DIR)/saeclib/src

SOURCES:=
SOURCES+= main.c
SOURCES+= $(SRC_DIR)/oscillator.c
SOURCES+= $(SAECLIB_DIR)/saeclib_circular_buffer.c

CFLAGS = -g -std=c99 -Wall -Wpedantic -lm -lportaudio -O0
CFLAGS+= -I$(SRC_DIR) -I$(SAECLIB_DIR)
CFLAGS+= -Wno-unused-function -Wno-unused-variable

cli_synth: $(SOURCES)
	$(CC) -o $@ $^ $(CFLAGS) $(LDFLAGS)
