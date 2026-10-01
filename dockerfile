FROM python:3.11-slim
WORKDIR /lab
COPY..
RUN mkdir -p app && touch app/waf.log
EXPOSE 8080
CMD ["python3", "main.py"]
