# Function to count characters, words, and lines in the file
def count_file_info(file_name):
    total_chars = 0
    total_words = 0
    total_lines = 0
    char_frequency = {}

    # Reading file and counting characters, words, lines, and character frequency
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            total_chars += len(line)
            total_words += len(line.split())
            total_lines += 1
            for char in line:
                if char in char_frequency:
                    char_frequency[char] += 1
                else:
                    char_frequency[char] = 1

    # Printing total characters, words, and lines
    print(f"Total characters: {total_chars}")
    print(f"Total words: {total_words}")
    print(f"Total lines: {total_lines}")

    # Printing character frequencies
    print("Character frequencies:")
    for char, freq in char_frequency.items():
        print(f"Character '{char}' appears {freq} times")

    # Reversing and printing words
    print("\nWords in reverse order:")
    for line in lines:
        words = line.split()
        for word in reversed(words):
            print(word[::-1], end=' ')

    # Copying even and odd lines to separate files
    with open('File1.txt', 'w') as file1, open('File2.txt', 'w') as file2:
        for i, line in enumerate(lines, 1):
            if i % 2 == 0:
                file1.write(line)
            else:
                file2.write(line)

# Usage
file_name = 'your_file.txt'  # Replace with your file name
count_file_info(file_name)
