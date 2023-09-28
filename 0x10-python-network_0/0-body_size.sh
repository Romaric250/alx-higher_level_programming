#!/bin/bash
# send a request url
curl -s "$1" | wc -c
