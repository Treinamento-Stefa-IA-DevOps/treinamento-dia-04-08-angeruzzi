FROM python:3.8-slim
#FROM centos/python-36-centos7

COPY . /codigo

WORKDIR /codigo

# instala as dependencias do python
RUN pip install pandas fastapi sklearn uvicorn[standart]

CMD ["uvicorn", "codigo.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]