FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5002
ENTRYPOINT [ "python", "app.py" ]