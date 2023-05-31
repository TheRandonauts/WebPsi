# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 58700

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN addgroup --gid 1024 appgroup
RUN adduser --disabled-password --gecos "" --gid 1024 appuser
RUN mkdir -p /app/logs
RUN chown :1024 /app/logs
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "-m", "webpsi"]
