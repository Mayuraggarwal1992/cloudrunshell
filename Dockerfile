FROM python:3.7

# Copy local code to the container image.
RUN mkdir p ~/cloudrun
COPY . ~/cloudrun
WORKDIR ~/cloudrun


# Install production dependencies.
RUN pip install requiements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 2 cloudrun:app