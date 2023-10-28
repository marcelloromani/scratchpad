.PHONY: all bin clean

all: hello_world quicksort

clean:
	rm -f *.o
	rm -f *.hi

bin:
	mkdir -p bin

hello_world: bin/hello_world
bin/hello_world: hello_world.hs
	ghc -o bin/hello_world hello_world.hs

quicksort: bin/quicksort
bin/quicksort: quicksort.hs
	ghc -o bin/quicksort quicksort.hs

