#!/bin/bash

gst-launch-1.0 -e \
    nvarguscamerasrc ! \
    "video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080, format=(string)NV12, framerate=(fraction)30/1" ! \
    queue ! \
    nvv4l2h264enc bitrate=8000000 ! \
    h264parse ! \
    flvmux ! \
    rtmpsink location="rtmp://localhost/rtmp/live live=1"
