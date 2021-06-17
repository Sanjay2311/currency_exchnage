FROM python:alpine

RUN mkdir -p /service/currencyConversion/
COPY currencyConversion.py /service/currencyConversion/
WORKDIR /service/currencyConversion/
RUN python -m pip install flask
RUN python -m pip install requests

EXPOSE 5000
ENV FLASK_APP=currencyConversion.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]