import re
import sys

# Function to convert seconds to HH:MM:SS.SSS format


def convert_seconds_to_hhmmss(match):
    if match is not None:
        seconds = float(match)
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = seconds % 60
        if seconds < 10:
            formatted_seconds = f"0{seconds:.3f}"
        else:
            formatted_seconds = f"{seconds:.3f}"
        formatted_time = f"{hours:02d}:{minutes:02d}:{formatted_seconds}"
        return formatted_time
    else:
        return match


# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python labels2chapters.py input_file.txt")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = "output.chapters.txt"

# Read input file and process text
with open(input_file_path, "r") as input_file:
    lines = input_file.readlines()

# Define a regular expression pattern to match columns separated by tabs
pattern = r"^(\S+)\s+(\S+)\s+(.*?)$"

# Process each line and replace seconds with the converted HH:MM:SS.SSS format
converted_lines = []
for line in lines:
    match = re.match(pattern, line)
    if match:
        start_time = match.group(1)
        title = match.group(3)
        converted_start_time = convert_seconds_to_hhmmss(match.group(1))
        converted_line = f"{converted_start_time}\n{title}\n"
        converted_lines.append(converted_line)
    else:
        converted_lines.append(line)

# Write the converted lines to the output file
with open(output_file_path, "w") as output_file:
    output_file.writelines(converted_lines)

print(f"Conversion completed. Output saved to '{output_file_path}'.")
