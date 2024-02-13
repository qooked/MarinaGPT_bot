FROM python:3
COPY requirements.txt .
RUN pip3 install -r requirements.txt --use-deprecated=legacy-resolver
COPY / .
CMD [ "python", "./main.py" ]