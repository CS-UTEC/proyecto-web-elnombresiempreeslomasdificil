#!/usr/bin/env bash

curl \
	--header "Content-Type: application/json" \
	--request POST \
	--data '{"user_id": 1, "markdown": "# Hello", "tags": ["a", "b"]}' \
	http://127.0.0.1:8080/recipes2
