# Website for testing Random Acts of Pizza Prediction

## Dependancies
Docker and docker-compose

## Website usage
```bash
# build
docker-compose build

# run
docker-compose up -d
```

## Run API tests
```bash
# build image for test
docker build --target test -t raop-demo:tests api/
# start container
docker run --rm --name raop_demo_test -d raop-demo:tests
# run api tests
docker exec raop_demo_test python -m unittest discover -v
```