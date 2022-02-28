
def count_words(this_string):
	return len(this_string.split())


if __name__ == "__main__":
	txt = "This is my new string to check words-like this"
	print(count_words(txt))

