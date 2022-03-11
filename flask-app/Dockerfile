
FROM python:3.7
WORKDIR /flask-app
COPY . .
# Install pip dependencies from requirements
RUN pip3 install -r requirements.txt
# Expose the correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT ["python", "app.py"]