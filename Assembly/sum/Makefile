# Makefile
all: $(SRC)
	./$(SRC) ; echo $$?

$(SRC): $(SRC).o
	gcc -o $@ $+

$(SRC): $(SRC).s
	as -o $@ $<

clean:
	rm -vf $(SRC) $(SRC).o
