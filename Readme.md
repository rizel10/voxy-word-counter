# install dependencies (Docker image will run the API, but frontend won't work with docker image)
pip install fastapi

# run api
cd path/to/app/
fastapi dev main.py

# open index.html in browser
Insert any text in the input and it should change counter value on button submit

# Running tests
pip install pytest
cd path/to/app/
pytest