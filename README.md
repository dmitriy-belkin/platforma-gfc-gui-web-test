# Platform GFC UI Test (WEB)


[![pipeline status](https://git.hrct.ru/qa/gfc-tests/badges/main/pipeline.svg)](https://gitlab.com/ruibeyd/platforma-gfc-gui-web-test/-/commits/main)
[![coverage report](https://git.hrct.ru/qa/gfc-tests/badges/main/coverage.svg)](https://gitlab.com/ruibeyd/platforma-gfc-gui-web-test/-/commits/main)
[![Latest Release](https://git.hrct.ru/qa/gfc-tests/-/badges/release.svg)](https://gitlab.com/ruibeyd/platforma-gfc-gui-web-test/-/releases)


#### Browsers support
- Chrome (default)
- Edge
- ~~FireFox~~ - not yet

## GitLab Usage
- To run job with Chrome just run pipeline with one of the Triggers
- To run job with Firefox set GitLab variable BROWSER=edge and run pipeline with one of the Triggers 

## Prepare (Allure)
### Linux
For debian-based repositories a PPA is provided:
```shell script
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update 
sudo apt-get install allure
```
### Windows
For Windows, Allure is available from the [Scoop](https://scoop.sh/) commandline-installer.

To install Allure, download and install Scoop and then execute in the Powershell:
```shell script
scoop install allure
```
Also Scoop is capable of updating Allure distribution installations. To do so navigate to the Scoop installation directory and execute
```shell script
\bin\checkver.ps1 allure -u
```
This will check for newer versions of Allure, and update the manifest file. Then execute
```shell script
scoop update allure
```
### Mac OS X
For Mas OS, automated installation is available via [Homebrew](https://brew.sh/)
```shell script
brew install allure
```

### Run with allure
```shell script
pytest --allure=./reports/
```
### Read allure
```shell script
allure serve ./reports/
```

## Local Usage
Prepare
```shell script
docker run -d -p 4444:4444 --net grid --name selenium-hub selenium/hub:3.141.59
docker run -d --net grid -e HUB_HOST=selenium-hub --name chrome -v /dev/shm:/dev/shm selenium/node-chrome
docker run -d --net grid -e HUB_HOST=selenium-hub --name firefox -v /dev/shm:/dev/shm selenium/node-firefox
docker run -d --net grid -e HUB_HOST=selenium-hub --name edge -v /dev/shm:/dev/shm selenium/node-edge
```

Run tests
```shell script
# tests on Chrome
pytest -s -v
# or
pytest --browser=chrome
# tests on Firefox 
pytest --browser=firefox
# tests on Edge 
pytest --browser=edge
```

End of work
```shell script
docker stop selenium-hub chrome firefox edge
```
