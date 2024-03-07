#!/bin/bash
#sends a request to a URL passed as an argument.
curl -s -o /dec/null -w "%{http_code}" "$1"
