# README #

This is dmc. It's an api layer for **DeLorean** app.

## How do I get set up? ##

```bash
pip install -r requirements.txt
```

### Running in Docker ###

There are two options to run:
- run dmc project;
- run **DeLorean** app.

1) To run dmc project in docker:

Linux OS:
```bash
docker compose up   # for development
```
```bash
docker compose up -f docker-compose.prod.yml  # for production
```

2) To run **DeLorean** app in docker:

Linux OS:

- create a new directory
    ```bash
  mkdir DeLoreanApp
    ```

- download *delorean* client repository 
    ```bash
  git clone ...
    ```
- download *dmc* server repository 
    ```bash
  git clone ...
    ```

- create symlinks
    ```bash
  ln -sf ./dmc/.docker/docker-compose.common.yml .
  ln -sf ./dmc/.docker/docker-compose.prod.common.yml .
    ```

- run docker
    ```bash
    docker compose up   # for development
    ```
    ```bash
    docker compose up -f docker-compose.prod.common.yml  # for production
    ```
