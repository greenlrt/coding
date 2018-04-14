# Makefile

all: $(SRC)

$(SRC): $(SRC).o
	gcc -o $@ $+

$(SRC).o: $(SRC).s
	as -o $@ $<

$(SRC).s: $(SRC).c
	gcc -S $^ -o $@

clean:
	rm -vf $(SRC) $(SRC).o $(SRC).s
