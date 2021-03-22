FROM python:3.9.2

ADD src /src

RUN pip install coverage

CMD [ "python", "./src/CalculatorTests.py" ]