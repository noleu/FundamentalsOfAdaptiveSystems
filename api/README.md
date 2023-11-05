## Requirements
* Docker

## Using the application

1. Build docker image
```console
$ docker build -t api .
```
2. Run docker container
```console
$ docker run -d -p 80:8000 api
```
3. Open browser and go to http://localhost:8000