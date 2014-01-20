#!/bin/bash

raspivid -o - -t 0 -hf -w 400 -h 200 -fps 6 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160/}' :demux=h264
#raspivid -o - -t 0 -hf -w 200 -h 100 -fps 10 |cvlc -vvv stream:///dev/stdin --sout '#transcode{vcodec=h264,mux=ts,width=400}:http{mux=mp4,dst=:8160/go.mp4}' 
 

