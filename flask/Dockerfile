# flud/flask/Dockerfile

FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy only the file necessary for pip install
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

VOLUME /app/app/static

# Copy the rest... (which is typically what changes...)
# NOTE: Do it w/ docker-compose during development
COPY . /app

ENV SQLALCHEMY_DATABASE_URI=mysql+pymysql://foo:foopa55@mysql/crud

# Run app.py when the container launches
CMD ["/usr/local/bin/gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "--access-logfile=-", "app:app"]