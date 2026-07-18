FROM python:3.12

WORKDIR /kubernetes-app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["python", "app.py"]
