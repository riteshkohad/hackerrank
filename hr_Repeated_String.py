
def repeated_string(this_string, this_number):
	int_total_length = len(this_string)
	int_repeating_number = int(this_number / int_total_length)
	int_leftover_chars = this_number % int_total_length

	int_total_char = (count_char_in_string(this_string,0) * int_repeating_number)

	if int_leftover_chars > 0:
		int_total_char += count_char_in_string(this_string, int_leftover_chars)

	return int_total_char


def count_char_in_string(this_string, this_length):
	str_use_this_string = this_string

	if this_length > 0:
		str_use_this_string = this_string[:this_length]

	return str_use_this_string.count("a")


if __name__ == '__main__':
	int_val = repeated_string("abcdefaadlkfasdfasklfdej asdfkj asdlfkj asdfl kjas dfl;sakj", 500)
	print(int_val)
