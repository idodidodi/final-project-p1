# Use the Python 3.13 slim image for a smaller footprint
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Flask needs to be told to listen on all interfaces to be reachable 
# outside the container.
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the default Flask port
EXPOSE 5000

# Run using the Flask CLI
CMD ["flask", "run"]