FROM python:3.8
RUN pip install streamlit
# COPY src/app.py /app/
COPY src/* /app/
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py"]

