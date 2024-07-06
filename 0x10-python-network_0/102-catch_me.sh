#!/bin/bash

# Make the request to the specified URL
curl -sL -X PUT -d "user_id=98" -H "Origin: school" 0.0.0.0:5000/catch_me
