FROM python:3.13-slim-bookworm
WORKDIR /app
RUN useradd --system --uid 10001 app
COPY app.py .
USER 10001
EXPOSE 8080
CMD ["python", "app.py"]
