FROM python:3.9-slim-buster
WORKDIR /app


# install python libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# launch website
FROM base as dev
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]

FROM base as test
RUN pip install requests && rm -r /root/.cache
COPY tests/ tests/
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]

FROM base as prod
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]