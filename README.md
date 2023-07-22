# GSPOTbackendtest
[![Automation](https://github.com/victoretc/GSPOTbackendtest/actions/workflows/Automation.yml/badge.svg)](https://victoretc.github.io/GSPOTbackendtest/)
[![Manual](https://github.com/victoretc/GSPOTbackendtest/actions/workflows/Manual.yml/badge.svg)](https://victoretc.github.io/GSPOTbackendtest/)
## Start project
1. Start docker-compose
```
docker-compose run autotests pytest --alluredir=allure-results
```
2. Start allure report
```
allure serve allure_results
```

## Commands
### Requirements 
Installing environments for Linux:
```
python3 -m venv venv 
source venv/bin/activate
```

Installing environments for Windows:
```
python3 -m venv venv 
venv/Scripts/activate
```

Installing requirements for Linux:
```
pip3 install -r requirements.txt
```

### Tests
Run tests:
```
pytest -s -v
```

### Allure
Windows install Allure:
```
scoop install allure
```

Generate Allure report:
```
pytest -s -v --alluredir=allure_results
```

Start Allure report:
```
allure serve allure_results
```

### Docker
Building docker container:
```
docker build -t autotests .
```

Running docker container:
```
docker run autotests
```

### Docker-compose
Running docker compose:
````
docker-compose run autotests pytest --alluredir=allure-results
`````