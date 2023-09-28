#!/bin/bash
# send a rewquest url and display status code. e.g 404, 302, etc
curl -s -o /dev/null -w "%{http_code}" "$1"
