FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY restaurant_env.py .
COPY graders.py .
COPY baseline_inference.py .
COPY README.md .
COPY openv.yaml .

# Just keep it running
CMD ["python", "-m", "http.server", "8000"]
