# Dockerfile
FROM python:3.9-slim
RUN pip install Flask pytz
COPY app.py /app.py
ENTRYPOINT ["python"]
CMD ["app.py"]