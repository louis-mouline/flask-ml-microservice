FROM python:3.9.7-slim-buster

# Working directory
WORKDIR /app

# Copy source code to working directory
COPY . application.py /app/

# Install packages from requirements.txt
RUN pip install --no-cache-dir --upgrade pip --user &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt --user

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "application.py" ]