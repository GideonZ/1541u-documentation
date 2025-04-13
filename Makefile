all: html

html:
	sphinx-build . ./build/

clean:
	rm -rf ./build/
