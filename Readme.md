## install dependencies (Docker image will run the API, but frontend won't work with docker image)
```sh
pip install fastapi
```

## run api
```sh
cd path/to/app/
fastapi dev main.py
```

## open index.html in browser
Insert any text in the input and it should change counter value on button submit

![alt text](/frontend2.png?raw=true)

## Running tests
```sh
pip install pytest
cd path/to/app/
pytest
```
