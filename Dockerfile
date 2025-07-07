#Use official python image
FROM python:3.10-slim

#set working directory
WORKDIR /app

#Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy the app code
COPY . .

#Expose the port Flask will run on
EXPOSE 5000

#Run the app
CMD [ "python", "app.py"]
