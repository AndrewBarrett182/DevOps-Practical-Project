FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5003
ENTRYPOINT [ "python", "app.py" ]