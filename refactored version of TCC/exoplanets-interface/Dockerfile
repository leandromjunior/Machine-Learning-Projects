FROM python:3.9

WORKDIR /main

RUN pip install xgboost

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

COPY src/ .

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]