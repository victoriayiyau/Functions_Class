#1
# my_name = "Lindsay"
# print list(my_name)

#2
# numbers = "1,2,3,4,5"
# split_numbers = numbers.split(",")
# print split_numbers

#3
# fish = "One fish two fish red fish blue fish"

# split_fish = fish.split("fish") #removes "fish"
# for i in range(len(split_fish)): #inspects every index in list
# 	split_fish[i] = split_fish[i].strip() #strips space from indexed item
# del split_fish[-1] #deletes last space which is in the last index
# print split_fish

#4

grocery_list = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quantity:1,price:4.49\n"]

def price_item (item_string):
	item_parts = item_string.split(",")
total_price = 0
for grocery_item in grocery_list:
	split_list[i] = split_list.split(":")

print split_list

# print split_list
# quantity_list = split_list[1].split(":")
# print quantity_list
# quantity = int(quantity_list[1])
# print quantity

# price_list = split_list[2].split(":")
# print price_list
# price = float(price_list[1])
# print price

# def bill(quantity, price):
# 	return quantity*price 

# print bill(quantity,price)






