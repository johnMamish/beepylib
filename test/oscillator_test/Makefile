CC = gcc

SRC_DIR =../../src
SAECLIB_DIR =$(SRC_DIR)/saeclib/src

SOURCES:=
SOURCES+= oscillator_test.c
SOURCES+= $(SRC_DIR)/oscillator.c
SOURCES+= $(SAECLIB_DIR)/saeclib_circular_buffer.c

CFLAGS = -g -std=c99 -Wall -Wpedantic -lm -O0
CFLAGS+= -I$(SRC_DIR) -I$(SAECLIB_DIR)
CFLAGS+= -Wno-unused-function -Wno-unused-variable

oscillator_test: $(SOURCES)
	$(CC) -o $@ $^ $(CFLAGS) $(LDFLAGS)
