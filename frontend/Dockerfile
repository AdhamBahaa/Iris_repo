FROM python:3.10-slim  

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

# "--server.enableCORS=false"
CMD ["streamlit", "run", "app.py", "--server.port=8501"] 
# CMD ["/bin/sh", "-c", "flask run --host=0.0.0.0 --port=5000 & streamlit run app.py"]