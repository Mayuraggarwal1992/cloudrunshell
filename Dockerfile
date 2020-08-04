FROM python:3.7

#Installing net-tools
RUN apt-get update && apt install net-tools && apt-get install traceroute

# Copy local code to the container image.
RUN mkdir p ~/cloudrun
COPY . ~/cloudrun
WORKDIR ~/cloudrun


# Install production dependencies.
RUN pip install --requirement requirements.txt
CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 2 cloudrun:app