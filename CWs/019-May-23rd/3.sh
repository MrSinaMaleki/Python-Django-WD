#!/bin/bash

read -a array -p "Enter a list of numbers: "

sum=0
count=0
for n in ${array[*]};
do
   ((sum+=$n)) && ((count++))

done

echo $(($sum / $count))
