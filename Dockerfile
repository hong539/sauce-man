#1st stage
#pull official base image
FROM docker.io/python:3.11.4-slim-bullseye

#set the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions
WORKDIR /app

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TOKEN Fj3RdeK7VTEgvQ6hvWeXMHsHYbu9KwAl21iTD6hjCa8iXydjwqhhT2PDrzqw91MD2I3sIhUh
ENV GUILD_ID 123456789012345678
ENV DB_USER test
ENV DB_HOST host
ENV DB_PASSWORD passwd
ENV DB_PORT port
ENV DB_NAME test_db

#COPY Django files needed
COPY requirements.txt /app
COPY /src /app

RUN pip install -r requirements.txt

# EXPOSE 8000
CMD ["python3", "main.py"]