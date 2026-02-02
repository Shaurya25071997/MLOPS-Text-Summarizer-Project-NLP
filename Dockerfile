FROM python:3.10-slim

WORKDIR /app

# Install awscli using pip (lightweight)
RUN pip install --no-cache-dir awscli

# Copy requirements first
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir transformers accelerate

# Copy app files
COPY . .

CMD ["python", "app.py"]
