import sys

def parse_entries(lines):
    keys_word = {}
    
    # Iterate through each line
    for line in lines:
        if not line.startswith('CHORD_LAYER('):
            continue
        line = line[len("CHORD_LAYER("):-1]
        # Extract the parameters from the line
        split_line = line.split(', ')
        word = split_line[0]  # Extract the chorded word, skipping every other element
        keys = split_line[2]  # Extract 'P_' keys, skipping every other element
        # Sort the keys to handle the order indifference
        sorted_keys = ' '.join(sorted(keys.split()))        
        # Add the line to the dictionary based on sorted keys
        if sorted_keys not in keys_word:
            keys_word[sorted_keys] = []
        keys_word[sorted_keys].append(word)
    return keys_word

def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def interactive_mode(parsed_lines):
    while True:
        user_input = input("Enter key combination (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break

        # Sort the keys to handle the order indifference
        user_input = ' '.join(sorted(user_input.split()))        

        if user_input in parsed_lines:
            print(f"Chords for key combination '{user_input}': {parsed_lines[user_input]}")
        else:
            print(f"No chords found for key combination '{user_input}'")

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
        parsed_lines = parse_entries(input_lines)

        # Find lines with the same parameters
        same_lines = dict(filter(lambda item: len(item[1]) >= 2, parsed_lines.items()))

        # Print the result if same_lines isn't empty
        if same_lines:
            print("Same parameters found:")
            for keys, chords in same_lines.items():
                print(f"  {keys}: {chords}")
            # Interactive mode
            interactive_mode(parsed_lines)
        else:
            print("# Chords::")
            for keys, chord in parsed_lines.items():
                print(f"  {chord}: {keys}")

                
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
