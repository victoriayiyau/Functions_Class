#parse file into strings - upper/lower/punction
#for loop in the list add, or else: count --> counting
#create dictionary (key = word; value = count)
#make dictionary.keys into list
#sort list  (alpha)
#(make dictionary.values into a list...?)
#write file
import collections

def clean_file_into_str_list():
	with open('LoremIpsum.txt') as my_file:
		my_data = my_file.read().decode("utf-8-sig").encode("utf-8")
		my_revised_data = my_data.replace(',', '').replace('.', '')
		my_data_list = my_revised_data.split(' ')
		new_list = []
		for item in my_data_list:
			new_list.append(item.lower())
		return new_list

def create_word_dict(new_list):
	word_dictionary = {}
	for word in new_list:
		if word in word_dictionary:
			word_dictionary[word] += 1
		else:
			word_dictionary[word] = 1
	return word_dictionary

def create_alpha_ordered_str(word_dictionary):
	return collections.OrderedDict(sorted(word_dictionary.items(), key=lambda t: t[0]))

def create_numeric_ordered_str(word_dictionary):
	return collections.OrderedDict(sorted(word_dictionary.items(), key=lambda t: t[1]))

def write_to_file(input_dictionary):
	with open('output.txt', 'w+') as my_file:
		for key in input_dictionary:
			output_text = key + ": " + str(input_dictionary[key]) + '\n'
			my_file.write(output_text)
	
def main():
	new_list = clean_file_into_str_list()
	word_dictionary = create_word_dict(new_list)
	new_alpha_dict = create_alpha_ordered_str(word_dictionary)
	new_num_dict = create_numeric_ordered_str(word_dictionary)
	# write_to_file(new_alpha_dict)
	write_to_file(new_num_dict)

if __name__ == '__main__':
	main()