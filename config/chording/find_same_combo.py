import sys
from itertools import combinations

def find_same_parameters(lines):
    parameter_lines = {}
    
    # Iterate through each line
    for line in lines:
        if not line.startswith('CHORD_LAYER('):
            continue
        # Extract the parameters from the line
        parameters = line.split(', ')[2]  # Extract 'P_' parameters, skipping every other element
        # Sort the parameters to handle the order indifference
        sorted_parameters = ' '.join(sorted(parameters.split()))        
        # Add the line to the dictionary based on sorted parameters
        if sorted_parameters not in parameter_lines:
            parameter_lines[sorted_parameters] = []
        parameter_lines[sorted_parameters].append(line)
    
    # Find lines with the same parameters
    result_lines = [lines for lines in parameter_lines.values() if len(lines) > 1]
    
    return result_lines

def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

if __name__ == "__main__":
    # Check if a file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
        sys.exit(1)

    # Get the file name from the command line
    file_name = sys.argv[1]

    try:
        # Read lines from the file
        input_lines = read_lines_from_file(file_name)

        # Find lines with the same parameters
        result = find_same_parameters(input_lines)

        # Print the result
        for lines in result:
            print("Same parameters found:")
            for line in lines:
                print(f"  {line}")

    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
