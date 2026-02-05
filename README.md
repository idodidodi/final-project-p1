# Final Project - Phase 1


## Declarative version
### A. Build the image - 
```bash
docker-compose build
```

### B. Run the container - Declarative
```bash
docker-compose up
```

## Imperative version
### A. Build the image - Imperative
```bash

docker build -t hello-flask:v1 .
```

### B. Run the container
```bash

docker run -d -p 5000:5000 hello-flask:v1
```

### Stop the container
```bash

docker stop <container_id>
```

    ## Remove the container
```bash

docker rm <container_id>
```

### Remove the image
```bash

docker rmi hello-flask:v1
```
