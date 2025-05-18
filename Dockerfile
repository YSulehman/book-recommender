# pull the python base image (check docker for which is suitable
FROM python:3.12-slim

# set the working directory (/app is convention)
WORKDIR /app

# install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the project files into the container (COPY <source> <destination>)
# COPY . .
COPY backend ./backend
COPY frontend ./frontend
# check the files are copied correctly
# RUN ls -lR backend
# RUN ls -lR frontend

# expose the port the app runs on (default uvicorn port is 8000)
EXPOSE 8000

# comand to run the app (general structure is "executable", "parameter")
# port 8000 more common for local development, port 80 for production
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
