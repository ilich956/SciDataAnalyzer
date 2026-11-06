# SciDataAnalyzer 🔬

![CI Pipeline](https://github.com/ilich956/SciDataAnalyzer/actions/workflows/ci.yml/badge.svg)

SciDataAnalyzer is a lightweight Python module designed for scientific data processing, statistical calculation, and automated visualization.

## Features
- **Data Processing:** Seamlessly converts raw dictionaries into Pandas DataFrames.
- **Statistical Analysis:** Automatically calculates Mean, Median, and Standard Deviation.
- **Visualization:** Generates publication-ready scatter plots using Matplotlib.
- **CI/CD Integrated:** Fully automated testing pipeline using GitHub Actions.

## Installation
Ensure you have Python 3.10+ installed, then run:
```bash
git clone https://github.com/ilich956/SciDataAnalyzer.git
cd SciDataAnalyzer
pip install -r requirements.txt```

## Docker
```bash
docker build -t scidataanalyzer .
docker run --rm scidataanalyzer                          # run the analysis
docker run --rm scidataanalyzer pytest test_analyzer.py  # run the tests
```

## Jenkins CI
The `Jenkinsfile` defines the pipeline: checkout, install dependencies, unit tests
(inside a `python:3.10-slim` container), Docker image build and image smoke test.
Jenkins polls the repository every minute, so every commit to `main` starts a build.

Start a local Jenkins server (bound to localhost only) with the job already configured:
```bash
cd jenkins
echo "JENKINS_ADMIN_PASSWORD=<choose-a-password>" > .env
docker compose up -d --build
```
Then open http://localhost:8080 and log in as `admin`.
