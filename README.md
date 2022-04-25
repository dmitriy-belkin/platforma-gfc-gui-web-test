# Platform GFC UI Test (WEB)



#### Browsers support
- Chrome (default)
- Firefox
- Edge

## GitLab Usage
- To run job with Chrome just run pipeline with one of the Triggers
- To run job with Firefox set GitLab variable BROWSER=edge and run pipeline with one of the Triggers 

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
