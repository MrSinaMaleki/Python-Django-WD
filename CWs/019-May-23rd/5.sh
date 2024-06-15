#!/bin/bash

echo "please enter your UID:"
read uid
user_info=$(getent passwd "$uid")
if [ -z "$user_info" ]; then
 echo "User with UID $uid does not exist."
 exit 1
fi
username=$(echo "$user_info" | cut -d: -f1)
home_directory=$(echo "$user_info" | cut -d: -f6)
shell=$(echo "$user_info" | cut -d: -f7)
group_number=$(echo "$user_info" | cut -d: -f4)
echo "Username: $username"
echo "Home Directory: $home_directory"
echo "Shell: $shell"
echo "Group Number: $group_number"