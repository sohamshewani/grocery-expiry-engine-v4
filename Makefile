all:
	@echo 'Available targets:'
	@echo '    test - Run tests'
	@echo '    build - Build the application'
	@echo '    clean - Clean up generated files'
test:
	@echo 'Running tests...'
	python3 -m unittest tests/
build:
	@echo 'Building the application...'
	python3 -m pip install -r requirements.txt

clean:
	@echo 'Cleaning up...'
	rm -rf build/
	rm -rf dist/
	rm -f grocery-expiry-engine.egg-info/