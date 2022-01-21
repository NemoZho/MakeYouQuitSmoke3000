# MakeYouQuitSmoke3000

## How to use
### On Jetson Nano
```console
~$ pip3 install -r ./on_nano/requirement.txt
```

```console
~$ docker run -d -it -p 1883:1883 -v $(pwd)/on_nano/end_smoke/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto 
~$ docker run -d -it -p 1884:1884 -v $(pwd)/on_nano/get_result/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
~$ python3 ./on_nano/get_result/get_result.py
~$ python3 ./on_nano/send_smoke/smoke.py
~$ ./stream/stream.sh
```
### On Server
```console
~$ pip3 install -r ./on_server/Smoke-Detect-by-yolov5_v2/requirement.txt
```

```console
~$ python3 ./on_server/Smoke-Detect-by-yolov5_v2/detect.py
```
