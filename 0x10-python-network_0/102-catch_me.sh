#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me server respond with You got me!
curl -sL -X PUT -H "Origin: You got me!" 0.0.0.0:5000/catch_me
