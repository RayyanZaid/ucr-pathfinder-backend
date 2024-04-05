FROM python:3-alpine3.15

WORKDIR /app

# Create the destination directory
RUN mkdir app

# Copy files into the destination directory
COPY . /app

# RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./server.py
