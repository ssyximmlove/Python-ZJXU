def add_line_numbers(input_filename, output_filename):  # 1
    try:  # 2
        with open(input_filename, 'r') as infile:  # 3
            lines = infile.readlines()  # 4
    except FileNotFoundError:  # 5
        print(f"Error: Input file '{input_filename}' not found.")  # 6
        return  # 7
    # 8
    num_lines = len(lines)  # 9
    line_number_width = len(str(num_lines))  # 10
    # 11
    with open(output_filename, 'w') as outfile:  # 12
        for i, line in enumerate(lines, 1):  # 13
            line_number = str(i).rjust(line_number_width)  # 14
            outfile.write(f"{line.rstrip()}  #{line_number}\n")  # 15


# 16
if __name__ == "__main__":  # 17
    input_filename = 'task1.py'  # 18
    output_filename = 'task1-new.py'  # 19
    add_line_numbers(input_filename, output_filename)  # 20
    print(f"Line numbers added. New file saved as '{output_filename}'")  # 21
