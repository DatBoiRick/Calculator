FROM python:3.9.2

ADD src /src

CMD [ "python", "./src/CalculatorTests.py" ]