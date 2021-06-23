FROM python:alpine

RUN mkdir -p /service/currencyExchange/
COPY currencyExchange.py /service/currencyExchange/
WORKDIR /service/currencyExchange/
RUN python -m pip install flask
RUN python -m pip install uuid

EXPOSE 3000
ENTRYPOINT [ "python", "currencyExchange.py" ]