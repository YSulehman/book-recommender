# pull the python base image (check docker for which is suitable
FROM python:3.10-slim

# set the working directory (/app is convention)
WORKDIR /app

# install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the project files into the container (COPY <source> <destination>)
COPY . .

# comand to run the app (general structure is "executable", "parameter")
# port 8000 more common for local development, port 80 for production
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
