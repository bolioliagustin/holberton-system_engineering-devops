#!/usr/bin/env bash
#script that takes in a URL, sends a request to that URL

curl -so /dev/null -w "%{size_download}" "$1"
