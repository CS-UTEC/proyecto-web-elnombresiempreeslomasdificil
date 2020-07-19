#!/usr/bin/env bash

curl \
	--header "Content-Type: application/json" \
	--request POST \
	--data '{"username": "a", "password": "b"}' \
	http://127.0.0.1:8080/users
