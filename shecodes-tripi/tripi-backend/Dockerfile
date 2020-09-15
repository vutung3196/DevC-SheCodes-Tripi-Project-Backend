FROM python:3.8-slim

ENV VIRTUAL_ENV=/usr/src/SheCodesApp
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app.py", "runserver", "-h", "0.0.0.0", "-p","8080"]