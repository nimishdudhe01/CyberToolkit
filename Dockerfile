FROM python:3.11.9-alpine3.19
RUN mkdir /root/app
WORKDIR /root/app
RUN pip install fastapi uvicorn sqlalchemy
COPY *.py *.sqlite .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
