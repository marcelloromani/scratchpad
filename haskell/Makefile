.PHONY: all bin clean

all: hello_world quicksort hello_you

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

hello_you: bin/hello_you
bin/hello_you: hello_you.hs
	ghc -o bin/hello_you hello_you.hs
