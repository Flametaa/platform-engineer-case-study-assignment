FROM python:3.11-slim

# Update packages
RUN apt-get update -y && apt-get upgrade -y
# Create non root user
RUN useradd -m myuser

WORKDIR /app

# Copy the Python script into the container
COPY url_link_extractor.py /app/

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Change to non root user
USER myuser

# Specify the entrypoint
ENTRYPOINT ["python", "/app/url_link_extractor.py"]