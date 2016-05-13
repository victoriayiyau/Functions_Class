SHOPPINGLIST = {}

menu_options ="""
0 - Main Menu
1 - Show all lists
2 - Show a specific list.
3 - Add a new shopping list.
4 - Add an item to a shopping list.
5 - Remove an item from a shopping list.
6 - Remove a list by nickname.
7 - Exit when you are done.
"""

def menu_choice():
	choice = int(raw_input("Please choose from the following menu: %s " % (menu_options)))

def show_list():
	global SHOPPINGLIST
	if SHOPPINGLIST == True:
		print SHOPPINGLIST.keys
	else:
		print "I don't have any Shopping List at the moment. Please add a new Shopping List"

def show_listcontents(key):
	#print value for specific key requested

def add_newlist(nickname):
	global SHOPPINGLIST
	if nickname in SHOPPINGLIST:
		print "%s already exists." % (nickname)
	else: 
		SHOPPINGLIST[nickname] = []
	print "%s has been created." % (nickname)
	
def add_item(nickname, item):
	global SHOPPINGLIST
	if nickname in SHOPPINGLIST:
		if item in SHOPPPINGLIST[nickname]:
			print "%s already exists." % (item)
		else:
			SHOPPINGLIST[nickname].append(item)
	else:
		print "That %s doesn't exist." % (nickname)
	
def remove_list(key):
	#check if key exists, if so, remove key
	#if no key exists, let user know
	
def remove_item(key, item):
	#check if key exists, if so, remove value from existing key
	#if no key exists, let user know

def sort_list(key):
	#sort list and print
	#lower and upper case???

def main():
	#For choice == 4:	
	choice_list = raw_input("To which shopping list would you like to add an item? ")
	choice_item = raw_input("What item(s) would you like to add?")
	add_item(choice_list.lower(), choice_item.lower())
	
	#add all menu choices with logic / conditionals / loops
	#break

if __name___ == '__main__':
	main()
