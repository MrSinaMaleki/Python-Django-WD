#!/bin/bash

echo "What word are you looking for? "
read word

echo "Please enter the name of your file. "
read filename

result = $(grep -c "$word" "$filename")
echo result
