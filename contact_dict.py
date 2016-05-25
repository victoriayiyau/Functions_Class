#create dict
#add entries - names = keys; list of num, email, birthday = values
#change index in value list
#change key: delete key, save value, create new key, assign to old value

contacts_dict = {}

contacts_dict['Diana Banana'] = ['(415)123-4567', 'diana@hackbrightacademy.com', '1970-02-16']
contacts_dict['Victoria Yau'] = ['(415)891-2345', 'victoria@gmail.com', '1980-01-17']


contacts_dict['Diana Banana'][0]='(888)888-8888'

def replace_name(key, new_key):
	old_name_list = contacts_dict[key]
	del contacts_dict[key]
	contacts_dict[new_key] = old_name_list
	return contacts_dict

replace_name('Victoria Yau', 'Victoria Williams')

print contacts_dict
