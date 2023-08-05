import os
def remove_comment_lines(file_path, output_path):
    try:
        with open(file_path, 'r') as input_file:
            lines = input_file.readlines()

        filtered_lines = [line for line in lines if not line.strip().startswith('/')]

        with open(output_path, 'w') as output_file:
            output_file.writelines(filtered_lines)

        print("Comment lines starting with '/' removed and saved to", output_path)

    except FileNotFoundError:
        print("File not found:", file_path)

# Replace 'input.sql' with your SQL file's path and 'output.sql' with the desired output file's path
remove_comment_lines('input.sql', 'output.sql')
