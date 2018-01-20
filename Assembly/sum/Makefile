compile: $(SRC).o
	gcc $? -o $(SRC)

assemble: $(SRC).s
	as $? -o $(SRC).o

run:
	./$(SRC) ; echo $$?
