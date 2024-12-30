help:
	@echo "make help            	- Prints this help message"
	@echo "make flake8				- Test flake8			"


run:
	fastapi run start.py --reload --host 0.0.0.0 --port 8001
	# fastapi dev start.py --host 0.0.0.0 --reload


