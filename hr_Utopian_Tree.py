
def find_ultopian_height(this_cycle):
	int_year = int(this_cycle / 2)
	int_height = (2 ** (int_year + 1)) - 1

	return int_height


if __name__ == '__main__':
	int_test_cycles = int(input("Enter test cycles: "))
	for i in range(int_test_cycles):
		int_period = int(input("Enter case: "))
		if int_period % 2 == 0:
			print(find_ultopian_height(int_period))
		else:
			print(find_ultopian_height(int_period - 1) * 2)





