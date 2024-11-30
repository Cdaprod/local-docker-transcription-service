FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

COPY app.py /app/

# Install Python dependencies
RUN pip install flask whisper openai langchain

EXPOSE 5000

CMD ["python", "app.py"]