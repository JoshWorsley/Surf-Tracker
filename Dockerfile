FROM python:3.12.0


WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt


COPY . .

EXPOSE 8000


ENTRYPOINT ["python", "SurfProject/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
