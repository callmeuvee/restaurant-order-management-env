FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY restaurant_env.py .
COPY graders.py .
COPY baseline_inference.py .

CMD ["python", "baseline_inference.py"]