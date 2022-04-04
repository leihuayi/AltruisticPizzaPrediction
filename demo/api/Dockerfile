FROM python:3.9-slim-buster
WORKDIR /app


# install python libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# launch website
COPY src/ src/
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]