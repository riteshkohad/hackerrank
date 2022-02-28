
def remove_duplicates_using_set(this_list):
	return list(set(this_list))


def remove_duplicates_using_dict(this_list):
	return list(dict.fromkeys(this_list))


if __name__ == "__main__":
	lst = [100, 150, 300, 300, 10, 20, 30,40, 50, 50, 60, 40]
	print(remove_duplicates_using_set(lst))
	print(remove_duplicates_using_dict(lst))

