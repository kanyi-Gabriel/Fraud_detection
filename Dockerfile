# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project directory into the container at /app/fraud_detection
# Note: Adjust the source path if your manage.py is not inside 'fraud_detection'
COPY fraud_detection/ /app/fraud_detection/

# Change the working directory to where manage.py is
WORKDIR /app/fraud_detection

# Expose port 8000 to allow communication to/from server
EXPOSE 8000

# Command to run the application using Gunicorn (more production-ready)
# If you don't have Gunicorn, you can use: CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# But first, add 'gunicorn' to your requirements.txt and rebuild
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fraud_detection.wsgi:application"]

# For now, let's stick with the development server:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]