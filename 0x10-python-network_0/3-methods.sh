#!/bin/bash
# display all http methods the server accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
