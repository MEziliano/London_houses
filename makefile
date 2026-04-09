.PHONY: help setup train serve api dashboard test clean

help:
	@echo "Available commands:"
	@echo "  make setup          Setup environment and install dependencies"
	@echo "  make train          Train all ML models"
	@echo "  make serve          Serve model predictions"
	@echo "  make api            Start FastAPI server"
	@echo "  make dashboard      Start Streamlit dashboard"
	@echo "  make test           Run tests"
	@echo "  make clean          Clean generated files"

setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

train:
	python scripts/run_training.py --config config/config.yaml

serve:
	python src/ml/pipeline/inference.py

api:
	uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

dashboard:
	streamlit run src/dashboard/app.py

test:
	pytest tests/ -v --cov=src --cov-report=html

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage