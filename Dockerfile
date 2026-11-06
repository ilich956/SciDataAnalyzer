# Container image for the SciDataAnalyzer research module
FROM python:3.10-slim

# Non-interactive Matplotlib backend (no display inside the container)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MPLBACKEND=Agg

WORKDIR /app

# Install pinned dependencies first to reuse the Docker layer cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code and tests
COPY sci_analyzer.py main.py test_analyzer.py ./

# Default command: run the analysis pipeline
CMD ["python", "main.py"]
