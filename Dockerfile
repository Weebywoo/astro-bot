FROM python:3.12.0-slim

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

COPY . .
RUN python -m pip install -r ./requirements.txt

# Run the application.
ENTRYPOINT ["python", "main.py"]
