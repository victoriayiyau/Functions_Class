from contact import*

contact_list = []

def add_contact(first_name, last_name):
	global contact_list
	new_contact = Contact(first_name,last_name) #instantiate instance of contact
	contact_list.append(new_contact) #add contact to contact_list

def remove_contact(first_name, last_name):
	global contact_list
	i = 0
	contact_deleted = 0
	while i < len(contact_list):
		if contact_list[i].last_name == last_name and contact_list[i].first_name == first_name: #checks if last name entered = last name in object in contact list
			del contact_list[i] #removes entire object
			contact_deleted += 1
			print "%s %s has been removed." % (first_name,last_name)
		else:
			i += 1 #continues to iterate
	if contact_deleted == 0:
		print "%s %s was not on the contact list." % (first_name,last_name)
	else:
		print "Here is your" #display contact list - insert function display_sorted

def search_contact(first_name, last_name):
	#searches contact list 
	global contact_list
	while True:
		print """Search Contact by: 
				1 - First Name
				2 - Last Name
				3 - Mobile Phone
				4 - Work Phone
				5 - Email
				6 - Twitter
				7 - Return to Main Menu"""
		search_option = raw_input("Please make your selection: ")
		search_text = raw_input("Enter text to search: ")
		i = 0
		while i < len(contact_list):
			if search_option == "1" and search_text == contact_list[i].first_name:
				show_contact(contact_list[i])
			elif search_option == "2" and search_text == contact_list[i].last_name:
				show_contact(contact_list[i])
			elif search_option == "3" and search_text == contact_list[i].mobile_number:
				show_contact(contact_list[i])
			elif search_option == "4" and search_text == contact_list[i].work_number:
				show_contact(contact_list[i])
			elif search_option == "5" and search_text == contact_list[i].email:
				show_contact(contact_list[i])
			elif search_option == "6" and search_text == contact_list[i].twitter_handle:
				show_contact(contact_list[i])
			elif search_option == "7":
				break
			
def show_contact(contact_object):
	print """First Name: %s 
			 Last Name: %s 
			 Mobile Phone: %s
			 Work Phone: %s
			 Email: %s
			 Twitter: %s 
			 """ % (contact_object.first_name, contact_object.last_name, contact_object.mobile_number, contact_object.work_number, contact_object.email, contact_object.twitter_handle)

def print_contact_list():
	#prints entire contact list
	global contact_list
	i = 0 
	while i < len(contact_list):
		show_contact(contact_list[i])
		i +=1

def edit_contact(first_name, last_name):
	global contact_list
	i = 0
	while i < len(contact_list):
		if contact_list[i].last_name == last_name and contact_list[i].first_name == first_name:
			show_contact(contact_list[i])
			while True:
				print """Edit Menu: 
						1 - First Name
						2 - Last Name
						3 - Mobile Phone
						4 - Work Phone
						5 - Email
						6 - Twitter
						7 - Return to Main Menu"""
				edit_menu_selection = raw_input("Please enter which information you would like to edit: ")
				if edit_menu_selection == "1": 
					#change First Name
					new_info = raw_input("Type new First Name: ")
					if new_info.strip(" ") == "":
						print "Invalid input. Please try again."
					else:
						contact_list[i].first_name = new_info
						print "First Name changed to %s." % (new_info)
				elif edit_menu_selection == "2":
					#change Last Name
					new_info = raw_input("Type new Last Name: ")
					if new_info.strip(" ") == "":
						print "Invalid input. Please try again."
					else:
						contact_list[i].edit_last_name(new_info)
						print "Last Name changed to %s." % (new_info)
				elif edit_menu_selection == "3":
					#change mobile phone
					new_info = raw_input("Type new Mobile Phone Number: ")
					if new_info.strip(" ") == "":
						print "Invalid input. Please try again."
					else:
						contact_list[i].edit_mobile_number(new_info)
						print "Mobile Number changed to %s." % (new_info)
				elif edit_menu_selection == "4":
					#change work phone
					new_info = raw_input("Type new Work Phone Number: ")
					if new_info.strip(" ") == "":
						print "Invalid input. Please try again."
					else:
						contact_list[i].edit_work_number(new_info)
						print "Work Number changed to %s." % (new_info)
				elif edit_menu_selection == "5":
					#change email
					new_info = raw_input("Type new Email Address: ")
					if new_info.strip(" ") == "":
						print "Invalid input. Please try again."
					else:
						contact_list[i].edit_email(new_info)
						print "Email changed to %s." % (new_info)
				elif edit_menu_selection == "6":
					#change twitter handle
					new_info = raw_input("Type new Twitter Handle: ")
					if new_info.strip(" ") == "":
						print "Invalid input. Please try again."
					else:
						contact_list[i].edit_twitter(new_info)
						print "Twitter Handle changed to %s." % (new_info)
				elif edit_menu_selection == "7":
					break 
				else:
					print "Invalid option. Please make another selection."
		i +=1

def main():
	while True:
		print """	
		Contact Manager Main Menu: 
		1 - Add New Contact
		2 - Remove Existing Contact
		3 - Edit Existing Contact
		4 - Show all Existing Contacts 				
		5 - Search Contact List
		6 - Exit
		"""
		menu_selection = raw_input("Please enter your selection from the Main Menu: ")
		if menu_selection == "1":
			#add contact
			first_name = raw_input("Please enter contact's First Name: ")
			last_name = raw_input("Please enter contact's Last Name: ")
			add_contact(first_name,last_name)
		elif menu_selection == "2":
			#remove contact
			first_name = raw_input("Please enter contact's First Name: ")
			last_name = raw_input("Please enter contact's Last Name: ")
			remove_contact(first_name,last_name)
		elif menu_selection == "3":
			#edit contact
			first_name = raw_input("Please enter contact's First Name: ")
			last_name = raw_input("Please enter contact's Last Name: ")
			edit_contact(first_name,last_name)
		elif menu_selection == "4":
			#show all contacts
			print_contact_list()
		elif menu_selection == "5":
			#search contact list
			search_contact(first_name,last_name)
		elif menu_selection =="6":
			break
	

if __name__ == '__main__':
	main()

