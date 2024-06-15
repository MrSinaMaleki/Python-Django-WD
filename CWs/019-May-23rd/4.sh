#read uid
#user_info=$(getent passwd "$uid")
#user_infoo=$(getent group "$uid")
#username=$(echo "$user_info" | cut -d: -f1)
#Home_dir=$(echo "$user_info" | cut -d: -f6)
#shell_num=$(echo "$user_info" | cut -d: -f7)
#group_list=$(echo "$user_info" | id -G -n "$username")
#group_num=$(echo "$group_list" | wc -w)
#echo "group list:"
#echo "$group_list"
#echo "group num:"
#echo "$group_num"
#echo "shell num:"
#echo "$shell_num"
#echo "person name:"
#echo "$username"
#echo "Home directory:"
#echo "$Home_dir"
