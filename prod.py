list_of_ints = [1, 7, 3, 4]
before_current = list_of_ints[:i]
after_current = list_of_ints[i+1:]
for i in range(list_of_ints):

	current = list_of_ints[i]
	prod = before_current* after_current
	before_current*=current
	after_current

