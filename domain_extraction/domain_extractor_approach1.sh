input_file="$1"
if [ ! -f "$input_file" ]; then
    echo "File not found!"
    exit 1
fi

sed 's/\(.*\)\.com.*/\1.com/' "$input_file" | awk -F'[/:.]+' '{print tolower($(NF-1)"."$NF)}' | sort -u
