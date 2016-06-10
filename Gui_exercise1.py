from Tkinter import *
'''
This is a simple GUI example.
There is a label, text entry box, and button.
When the button is clicked, a function is executed.
Limitations - If I wanted to create many instances of this GUI,
I would have to duplicate this code over and over.
'''

class NameBox(object):
	def __init__(self, master):
		self.master = master
		self.clicked_already = False
		self.var_label_text = StringVar(master)          # Special Tkinter Variable for label text
		self.var_label_text.set("Display your full name here.")
		lbl_hello = Label(master, textvariable=self.var_label_text).grid(row=0, column=1)

		# var_label_First.set("First")
		lbl_First = Label(master, text="First").grid(row=1, column=0)

		# var_label_Last.set("Last")
		lbl_Last = Label(master, text="Last").grid(row=2, column=0)

		self.entry_text = Entry(master)                 # creates a text entry box
		self.entry_text.insert(0, "Type First Name")
		self.entry_text.grid(row=1, column=1, sticky=E)   # text to display on start up

		self.entry_text2 = Entry(master)                        # creates a text entry box
		self.entry_text2.insert(0, "Type Last Name")
		self.entry_text2.grid(row=2, column=1, sticky=E)   # text to display on start up

		# create a button
		# command sets a function to run when the button is clicked. AKA as an event and callback
		self.btn_label = StringVar(master)
		self.btn_label.set('Ok')
		self.btn_ok = Button(master, textvariable=self.btn_label, command=self.number_clicked).grid(row=3, column=1)

	def number_clicked(self):
		if self.clicked_already == False:
			self.var_label_text.set("My name is " + self.entry_text.get()+ " " + self.entry_text2.get())
			self.clicked_already = True
			self.btn_label.set('Close')
		else:
			self.master.destroy()

def main():
	root_widget = Tk()                          # creates a widget window which will hold all other widgets.
	root_widget.geometry("230x100")             # sets the size of the window
	root_widget.title("Simple GUI Demo")        # set the title of the window
	app = NameBox(root_widget)

# runs the window in a loop so it continuously detects the button click event
	root_widget.mainloop()

if __name__ == '__main__':
	main()