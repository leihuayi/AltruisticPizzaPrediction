# Raopdemo Vue.js frontend

## Project setup
### Without Docker
```bash
# install requirements
npm install

# Compiles and minifies for production
npm run build

# Lints and fixes files
npm run lint
```
### With Docker
```bash
docker build --target dev -t raopdemo-client:dev .
```

## Run project
### Without Docker
```bash
npm run serve
```

### With Docker
```bash
docker run --rm -p 8080:8080 -d raopdemo-client:dev
```


### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
