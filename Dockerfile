# 
FROM python:3.11

# 
WORKDIR /code

# 
RUN pip install --no-cache-dir --upgrade fastapi

# 
COPY ./app /code/app

# 
CMD ["fastapi", "run", "app/main.py", "--port", "80"]