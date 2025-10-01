# Stage 1: Build stage
FROM python:3.10-slim AS builder

WORKDIR /app

# Install build tools and pip packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install dependencies to a target directory
RUN pip install --upgrade pip && pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.10-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY . .

# Expose port
EXPOSE 8000

# Start FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



#docker build -t ml-fastapi-app .
#docker run -p 8000:8000 ml-fastapi-app
