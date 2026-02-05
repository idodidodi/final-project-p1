# Final Project - Phase 1

## Build the image
```bash

docker build -t hello-flask:v1 .
```

## Run the container
```bash

docker run -d -p 5000:5000 hello-flask:v1
```

## Stop the container
```bash

docker stop <container_id>
```

    ## Remove the container
```bash

docker rm <container_id>
```

## Remove the image
```bash

docker rmi hello-flask:v1
```
