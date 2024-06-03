# Use the official Python image as base
FROM python:3.9

# Set working directory in the container
WORKDIR /order_capture

# Copy the requirements file
COPY ./requirements.txt /order_capture/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the application files to the container
COPY ./app /order_capture/app

# Expose the port that FastAPI runs on
EXPOSE 8001

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app","--proxy-headers", "--host", "0.0.0.0", "--port" ,"8001"]
