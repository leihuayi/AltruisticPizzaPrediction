FROM python:3.9-slim-buster as base
WORKDIR /app


# install python libraries
COPY requirements.txt .
RUN pip install --index-url https://test.pypi.org/simple/ \
                --extra-index-url https://pypi.org/simple/ \
                -r requirements.txt \
    && rm -r /root/.cache
COPY src/ src/

# launch website
FROM base as dev
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]

FROM base as test
RUN pip install requests
COPY tests/ tests/
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]

FROM base as prod
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]