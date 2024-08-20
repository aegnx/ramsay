# Using a slim python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the ramsay.py file 
COPY ramsay.py .

# Create a non-root user
RUN addgroup --system appgroup \
    && adduser --system --ingroup appgroup --no-create-home appuser

# Set the user
USER appuser

# Run the script
CMD ["python", "ramsay.py"]
