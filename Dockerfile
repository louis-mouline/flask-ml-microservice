FROM python:3.9.7-slim-buster

# Working directory
WORKDIR /app

# Copy source code to working directory
COPY . app.py /app/

# Install packages from requirements.txt
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]