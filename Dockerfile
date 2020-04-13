From python:3.8

RUN pip install requests
RUN pip install flask

COPY testflask.py ./testflask.py

EXPOSE 80

CMD ["python", "testflask.py"]
