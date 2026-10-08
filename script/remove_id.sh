#!/bin/bash

input_dir="/home/thant_syn/exp/polar/processed"

for file in "$input_dir"/*.txt; do
    output="${file%.txt}_no_id.txt"

    cut -d'|' -f2- "$file" > "$output"

    echo "Processed: $(basename "$file")"
done

echo "Done!"
