import string

encrypt_dict = {}
decrypt_dict = {}

def create_code_dictionaries():
	global encrypt_dict
	global decrypt_dict

	count = 100
	for character in string.printable:
		encrypt_dict[character] = "{:03}".format(count)
		decrypt_dict["{:03}".format(count)] = character
		# Increment the code
		count -= 1

def encrypt(message):
	global encrypt_dict
	   
	if message == "":
		print "Sorry the message is empty."
	else:
		new_message = ""

		for character in message:
			new_message += encrypt_dict[character]

		return new_message

def decrypt(message):
	global decrypt_dict
	
	if message == "":
		print "Sorry the message is empty."
	else:
		new_message = ""

		for code in range(0,len(message),3):
			new_message += decrypt_dict[message[code:code+3]]

		return new_message

def main():
	create_code_dictionaries()

	user_message = raw_input("Type the message you would like to encrypt: ")

	new_message = encrypt(user_message)

	print "\nYour original message is:\n" + user_message
	print "\nYour encrypted message is:\n" + new_message

	original_message = decrypt(new_message)
	
	print "\nYour decrypted message is:\n" + original_message

if __name__ == "__main__":
	main()