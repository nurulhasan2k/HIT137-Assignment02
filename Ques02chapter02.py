input_string = 'A2b3C4d5E6f7G8h9I0J'

number_substring = ''.join([ch for ch in input_string if ch.isdigit()])
letter_substring = ''.join([ch for ch in input_string if ch.isalpha()])

even_numbers = [int(num) for num in number_substring if int(num) % 2 == 0]

ascii_even_numbers = [ord(str(num)) for num in even_numbers]

uppercase_letters = [ch for ch in letter_substring if ch.isupper()]

ascii_uppercase_letters = [ord(ch) for ch in uppercase_letters]

print("Numbers in ASCII decimal value:", ascii_even_numbers,"\n","Letters in ASCII decimal value: ", ascii_uppercase_letters)