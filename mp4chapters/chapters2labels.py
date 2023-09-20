import re
import sys

# Function to convert HH:MM:SS.SSS format to seconds


def convert_hhmmss_to_seconds(match):
    if match is not None:
        match = match.split(":")
        hours = float(match[0])
        minutes = float(match[1])
        seconds = float(match[2])
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds
    else:
        return match


# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python chapters2labels.py input_file.txt")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = 'output.labels.txt'

# Read input file and process text
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

# Define a regular expression pattern to match HH:MM:SS.SSS format
pattern = r'^(\d{2}:\d{2}:\d{2}.\d{3})\s+(.*?)$'

# Process each line and replace HH:MM:SS.SSS format with seconds
converted_lines = []
for line in lines:
    match = re.match(pattern, line)
    if match:
        start_time = match.group(1)
        title = match.group(2)
        converted_start_time = convert_hhmmss_to_seconds(match.group(1))
        converted_line = f"{converted_start_time}\t{title}\n"
        converted_lines.append(converted_line)
    else:
        converted_lines.append(line)

# Write the converted lines to the output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(converted_lines)

print(f"Conversion completed. Output saved to '{output_file_path}'.")
