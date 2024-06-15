


if [ -d "$file" ] ; then
    echo "$file is a directory";
else
    if [ -f "$file" ]; then
        echo "$file is a file";
        if [[ -x "$file" ]]
        then
            echo "File '$file' is executable"
        else
            echo "File '$file' is not executable or found"
        fi
    else
        echo "$file is not valid(not a file or directory)";
        exit 1
    fi
fi




