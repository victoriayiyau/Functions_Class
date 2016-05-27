from contact import*

contact_list = []

def add_contact(first_name, last_name):
	global contact_list
	new_contact = Contact(first_name,last_name) #instantiate instance of contact
	contact_list.append(new_contact) #add contact to contact_list

# def remove
# #check if contact exists in list, if yes, remove; if no, display warning
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
			i += 1
	if contact_deleted == 0:
		print "%s %s was not on the contact list." % (first_name,last_name)
	else:
		print "Here is your" #display contact list - insert function display_sorted
			
def edit(first_name, last_name):
	global contact_list
	old_contact = Contact(first_name, last_name)
	if old_contact in contact_list:
		new_contact = contact_list.index(old_contact)
		print "%s has replaced %s in the contact list." % (new_contact, old_contact)
	else:
		print "%s is not in the contact list." % (old_contact)
		
# def edit
# #check if contact exists in list, if yes, edit contact attributes, if no, create new instance of contact

# def display_sorted
# #print contact_list

def main():
	first_name = "Wendy" #raw_input("Please type contact's first name: ")
	last_name = "Brown" #raw_input ("Please type contact's last name: ")
	print add_contact(first_name, last_name)
	print remove_contact(first_name, last_name)
	# # edit(first_name, last_name)
	# return contact_list

main()




	
	# more_info = raw_input("Do you want to add more contact details?")
	# if more_info.upper == "YES":
	# 	edit()
	# else:
	# 	print new_contact