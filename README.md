[![Python application](https://github.com/krakenbite/python-containerized-microservice/actions/workflows/ci.yml/badge.svg)](https://github.com/krakenbite/python-containerized-microservice/actions/workflows/ci.yml)

# Containerized Microservice

## Overview

This is a small containerized microservice, which is built with
[Python](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/)
and is containerized with [Docker](https://www.docker.com/).
FastAPI is a web framework used to build Web APIs with Python.

This microservice contains one route ("< base-path >: < port >/v1/target-exists"), which
is a POST endpoint. It expects a JSON body of the form

```
{
    "a": list[int],
    "b": list[int],
    "target": int
}
```

It calculates if there is an integer $a_i$ in list a and an integer $b_j$ in
list b such that $a_i + b_j = target$. If so, it returns the value `True`.
`False` otherwise.

## Prerequisites

This project has some expectations about the environment. To be able to run it,
the following tools need to be installed on the system:

- [Python](https://www.python.org/) (tested with Python v3.11)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)

## Starting the container
To start the container, just type
```
./startup.sh
```

It should now build the poetry app and build and spin up the container. 
As soon as it is started, it should state
`Uvicorn running on http://0.0.0.0:8080`. It is now ready to be called by the
user.

One can call it with a cURL command like this:

```
curl localhost:8080/v1/target-exists --data '{ "a": [1,2,3], "b": [4,5,6], "target": 9 }' -H 'content-type: application/json'
```

It should return `true`. Feel free to try out other combinations!