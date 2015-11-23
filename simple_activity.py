"""Assumes perfect user-input!"""

from Tkinter import *
import datetime 
from datetime import time, date
import time
import convert

root = Tk()
_ACTIVITY_LOG = []


def button_evaluate(int):
	"""Returns a string value for the integer value returned from evaluating the buttons in tKinter."""
	done = None 
	if int is 0: 
		done = 'started'
	if int is 1:
		done = 'finished'
	return done


def enter_data():
	"""Collects text from user entry."""
	# Appends the activity and start | stop in the list activity_log 
	_ACTIVITY_LOG.append((ent.get(), v.get(), datetime.datetime.time(datetime.datetime.now())))
	print  "The latest entry: ", _ACTIVITY_LOG[-1][0], button_evaluate(_ACTIVITY_LOG[-1][1]), _ACTIVITY_LOG[-1][2]
	if v.get() == 1: 
		if len(_ACTIVITY_LOG) >= 2:
			record_time(ent.get(), _ACTIVITY_LOG[-2][2], _ACTIVITY_LOG[-1][2])
		# Clear the _ACTIVITY_LOG list if the user is finished the activity
		del _ACTIVITY_LOG[:]


def record_time(activity, start, end):
	"""Returns the difference between of the end time and start time and records the information in file f."""
	time = datetime.datetime.combine(date.today(), end) - datetime.datetime.combine(date.today(), start) # Length of time it takes for the activity 
	print "Time took: %s hours %s minutes %s seconds" % convert.convert_seconds(time.seconds)
	with open('workfile.txt', 'a') as f: 
		f.write('%s/%s/%s\n' % (activity, convert.convert_seconds(time.seconds), start)) # Avoiding comma as delimter because of the tuple
		

# Create the header message
message_content = 'This is your activity tracker from Squirrel Technologies. Log your activity in the box below.'
msg = Message(root, width='1000', text = message_content)
msg.config(bg='lightblue', justify=LEFT, font=('baskerville', '16'))
msg.pack()
# Create the quit and enter buttons
b2 = Button(root, text='Quit', command=root.quit)
b2.pack(side=RIGHT, padx=5, pady=5)
b1 = Button(root, text='Enter', command=enter_data)
b1.pack(side=RIGHT, padx=5, pady=5)
# Create the 'Activity' entry form 
row = Frame(root)
lab = Label(row, width=25, bg='lightblue', text='Activity', anchor='w')
ent = Entry(row)
row.pack(side=TOP, fill=X, padx=5, pady=5)
lab.pack(side=LEFT)
ent.pack(side=RIGHT, expand=YES, fill=X)
# Create Buttons
v = IntVar()
v.set(1)
options = [('Starting', 0), ('Finishing', 1)]
for txt, val in options:
	Radiobutton(root,
		text=txt,
		font=('baskerville', '14'),
		justify = LEFT,
		padx = 20,
		variable=v,
		value=val).pack(anchor=W)

mainloop()

