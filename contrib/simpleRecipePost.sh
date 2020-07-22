#!/usr/bin/env bash

curl \
	--header "Content-Type: application/json" \
	--request POST \
	--data '{"user_id": 1, "title": "Hello", "description": "abc"}' \
	http://127.0.0.1:8080/recipes
