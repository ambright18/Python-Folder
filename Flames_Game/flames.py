
def remove_match_char(list1, list2):

	for index in range(len(list1)):
		for j in range(len(list2)):
			if list1[index] == list2[j]:
				character = list1[index]

				# remove character from the list
				list1.remove(character)
				list2.remove(character)

				list3 = list1 + ["*"] + list2

				return [list3, True]

	list3 = list1 + ["*"] + list2
	return [list3, False]


# Driver code
if __name__ == "__main__":

	# take first name
	player1 = input("Player 1 name : ")

	# converted all letters into lower case
	player1 = player1.lower()

	# replace any space with empty string
	player1.replace(" ", "")

	# make a list of letters or characters
	player1_list = list(player1)

	player2 = input("Player 2 name : ")
	player2 = player2.lower()
	player2.replace(" ", "")
	player2_list = list(player2)

	# taking a flag as True initially
	proceed = True

	while proceed:
		ret_list = remove_match_char(player1_list, player2_list)

		con_list = ret_list[0]
		proceed = ret_list[1]
		star_index = con_list.index("*")

		player1_list = con_list[: star_index]
		player2_list = con_list[star_index + 1:]

	count = len(player1_list) + len(player2_list)

	# list of FLAMES acronym
	result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
	
	while len(result) > 1:

		split_index = (count % len(result) - 1)
		if split_index >= 0:
			right = result[split_index + 1:]
			left = result[: split_index]

			result = right + left

		else:
			result = result[: len(result) - 1]

	# print final result
	print("Relationship status :", result[0])
