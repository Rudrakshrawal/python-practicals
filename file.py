def count_chars_words_lines(file_name):
    # Opening the file in read mode
    with open(file_name, 'r') as file:
        content = file.read()

        # Counting characters, words, and lines
        num_chars = len(content)
        num_words = len(content.split())
        num_lines = content.count('\n') + 1

        print(f"Total characters: {num_chars}")
        print(f"Total words: {num_words}")
        print(f"Total lines: {num_lines}")

        # Counting frequency of each character
        char_frequency = {}
        for char in content:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

        print("Character frequencies:")
        for char, freq in char_frequency.items():
            print(f"'{char}': {freq}")

        # Reversing words
        words = content.split()
        reversed_words = ' '.join(words[::-1])
        print("\nWords in reverse order:")
        print(reversed_words)

        # Copying even and odd lines to different files
        with open('File1', 'w') as file1, open('File2', 'w') as file2:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if i % 2 == 0:
                    file1.write(line + '\n')
                else:
                    file2.write(line + '\n')


# Usage:
file_name = 'your_file.txt'  # Replace 'your_file.txt' with your file name
count_chars_words_lines(file_name)