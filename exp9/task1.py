def add_line_numbers(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return

    num_lines = len(lines)
    line_number_width = len(str(num_lines))

    with open(output_filename, 'w') as outfile:
        for i, line in enumerate(lines, 1):
            line_number = str(i).rjust(line_number_width)
            outfile.write(f"{line.rstrip()}  #{line_number}\n")


if __name__ == "__main__":
    input_filename = 'task1.py'
    output_filename = 'task1-new.py'
    add_line_numbers(input_filename, output_filename)
    print(f"Line numbers added. New file saved as '{output_filename}'")
