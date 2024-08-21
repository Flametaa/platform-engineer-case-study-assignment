input_file="$1"
if [ ! -f "$input_file" ]; then
    echo "File not found!"
    exit 1
fi

grep -oE '[a-zA-Z0-9-]+\.com' $input_file | tr '[:upper:]' '[:lower:]' | sort -u
