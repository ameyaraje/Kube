FROM basepy:latest

# RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip3 install -r requirements.txt

EXPOSE 9000
CMD ["python3", "/app/app.py"]