From python:3.6-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

RUN python make.py
ENV FLASK_APP=app
ENV FLASK_ENV=development

EXPOSE 8000
CMD ["flask run --host 0.0.0.0 --port 8000"]