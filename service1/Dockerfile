FROM python:3.7
RUN apt update
RUN apt install python3-pip -y
COPY . .
RUN pip install -r requirements.
EXPOSE 5000
ENTRYPOINT [ "python", "app.py" ]