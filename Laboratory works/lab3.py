from math import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style	
import matplotlib.pyplot
from tkinter import *
from tkinter import messagebox, ttk
import numpy as np

matplotlib.use("TkAgg")
style.use("ggplot")
error_code = 10000000000000000

# d_option == 0: f(x)
# d_option == 1: f'(x)
def f1(x, d_option=0):
    if d_option == 0:
        return np.sin(x)
    elif d_option == 1:
        return np.cos(x)


# Finding the derivative value of a function
def derivative(x, d_option = 0):
    # return (f1(x + dx, d_option) - f1(x, d_option)) / dx
    if d_option == 0:
    	return f1(x, 1)
    else:
    	return -f1(x, 0)


def secant_method(x, e, maxI, d_option = 0):
    count = 0
    while True:
        x1 = x - f1(x, d_option) / derivative(x, d_option)
        if abs(x1 - x) < e:
            break
        x = x1
        count += 1
        if count >= maxI:
            return (error_code, error_code)
    return (x, count)


# Plotting the function
def draw_graphic(d_option):
    a.cla()
    start = float(se1.get())
    end = float(se2.get())
    step = 0.001
    t1 = np.arange(start, end, step)
    a.plot(t1, f1(t1))

    # Drawing roots
    if d_option == 0:
	    while True:
	        if start >= end:
	            break
	        res, res1 = secant_method(start, 0.01, 100)
	        if res != error_code and start <= res < start + step:
	        	a.scatter(res, f1(res), color='r')
	        start += 0.01

    # Drawing extremums
    else:
	    while True:
	        if start >= end:
	            break
	        res, res1 = secant_method(start, 0.01, 100, 1)
	        if res != error_code and start <= res < start + step:
	        	a.scatter(res, f1(res), color='b')
	        start += 0.01      

    canvas.draw()


# Plotting root and making the table of roots
def draw_root_table():
    tree.heading('#2', text='Root')
    tree.column("#2", minwidth=50, width=100)
    # Clearing tree
    for child in tree.get_children():
        tree.delete(child)

    draw_graphic(0)
    # Getting all the values from entries
    eps = float(eEntry.get())
    start = float(se1.get())
    end = float(se2.get())
    step = float(step_Entry.get())
    maxI = int(iter_Entry.get())
    count = 1

    # Processing loop
    while True:
        if start >= end:
            break
        step1 = 0.01
        count1 = 0
        while True:
        	res, res1 = secant_method(start + step1 * count1 , eps, maxI)
        	if start <= res < start + step: 
        		break
        	if start + step1 * count1 >= start + step:
        		break
        	count1 += 1

        print(res)
        if start == -0.1:
        	start += step
        	continue
        if res == error_code:
            tree.insert("", count - 1, text=str(count), values=(
                '{:5.2f} -> {:5.2f}'.format(start, min(start + step, end)), '__', '__', '__', '#1'))
            count += 1
        elif start <= res < min(start + step, end):
            tree.insert("", count - 1, text=str(count), values=(
                '{:5.2f} -> {:5.2f}'.format(start, min(start + step, end)), '{:5.2f}'.format(res), '{:0.0E}'.format(f1(res)), str(res1), '#0'))
            count += 1
        start += step


# Plotting root and making the table of extremums
def draw_extremum_table():
    tree.heading('#2', text='Extremum')
    tree.column("#2", minwidth=50, width=100)
    # Clearing tree
    for child in tree.get_children():
        tree.delete(child)

    draw_graphic(1)
    # Getting all the values from entries
    eps = float(eEntry.get())
    start = float(se1.get())
    end = float(se2.get())
    step = float(step_Entry.get())
    maxI = int(iter_Entry.get())
    count = 1

    # Processing loop
    while True:
        if start >= end:
            break

        step1 = 0.01
        count1 = 0
        while True:
        	res, res1 = secant_method(start + step1 * count1 , eps, maxI, 1)
        	if start <= res < start + step: 
        		break
        	if start + step1 * count1 >= start + step:
        		break
        	count1 += 1

        print(res)
        if res == error_code:
            tree.insert("", count - 1, text=str(count), values=(
                '{:5.2f} -> {:5.2f}'.format(start, min(start + step, end)), '__', '__', '__', '#1'))
            count += 1
        elif start <= res < min(start + step, end):
            tree.insert("", count - 1, text=str(count), values=(
                '{:5.2f} -> {:5.2f}'.format(start, min(start + step, end)), '{:5.2f}'.format(res), '{:0.0E}'.format(f1(res)), str(res1), '#0'))
            count += 1
        start += step


# Showing the infomation about error codes
def error_info():
    messagebox.showinfo("Error Information",
                        "#0: No error\n#1: Time limit exceeded\n#2: Root(Extremum) out of range")


"""Configuring root"""
root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
for row_index in range(12):
    Grid.rowconfigure(root, row_index, weight=1)
for column_index in range(4):
    Grid.columnconfigure(root, column_index, weight=1)

"""Creating Graph"""
f = Figure(figsize=(4, 2), dpi=100)
a = f.add_subplot('111', title='Graphic')

canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0, rowspan=9, sticky='nsew')
canvas._tkcanvas.grid(row=1, column=0, rowspan=9, sticky='nsew')

"""Creating toolbar"""
toolbar_frame = Frame(root)
toolbar_frame.grid(row=10, column=0)
toolbar = NavigationToolbar2TkAgg(canvas, toolbar_frame)
toolbar_frame.update()

"""Creating Functions Checkboxes"""
checkbox_frame = Frame(root)
checkbox_frame.grid(row=1, column=1, rowspan=3, columnspan=2, sticky='nsew')
checkbox_Label = Label(checkbox_frame, text='Functions: F(x)= sin(x)')
checkbox_Label.grid(row=0, column=0, sticky='w')
var1 = IntVar()


"""Creating Algorithms Checkboxes"""
algorithm_frame = Frame(root)
algorithm_frame.grid(row=4, column=1, rowspan=3, columnspan=2, sticky='nsew')
algorithm_Label = Label(algorithm_frame, text='Algorithms: Secant')
algorithm_Label.grid(row=0, column=0, sticky='w')
var2 = IntVar()

"""Creating Entries"""
# Epsilon
eLabel = Label(root, text="Epsilon")
eEntry = Entry(root, width=12)
eLabel.grid(row=7, column=1, sticky='w')
eEntry.grid(row=7, column=2, columnspan=3, sticky='we')

# Section
s1 = Label(root, text="Section        [")
s2 = Label(root, text=",")
s3 = Label(root, text="]")
se1 = Entry(root, width=5)
se2 = Entry(root, width=5)
s1.grid(row=8, column=1, sticky='w')
se1.grid(row=8, column=2, sticky='we')
s2.grid(row=8, column=3, sticky='w')
se2.grid(row=8, column=4, sticky='we')
s3.grid(row=8, column=5, sticky='w')

# Step
step_Label = Label(root, text="Step")
step_Entry = Entry(root, width=12)
step_Label.grid(row=9, column=1, sticky='w')
step_Entry.grid(row=9, column=2, columnspan=3, sticky='we')

# Max iterator
iter_Label = Label(root, text="Max. iterator")
iter_Entry = Entry(root, width=12)
iter_Label.grid(row=10, column=1, sticky='w')
iter_Entry.grid(row=10, column=2, columnspan=3, sticky='we')

"""Creating Buttons"""
btn1 = Button(root, text='Root', command=draw_root_table, height=3).grid(
    row=11, column=1, columnspan=4, sticky='nsew')
btn2 = Button(root, text='Extremum', command=draw_extremum_table, height=3).grid(
    row=12, column=1, columnspan=4, sticky='nsew')
btn3 = Button(root, text='Error Information', command=error_info, height=3).grid(
    row=13, column=1, columnspan=4, sticky='nsew')

"""Creating treeview"""
treeview_frame = Frame(root)
treeview_frame.grid(row=11, column=0, rowspan=4, sticky='nsew')
tree = ttk.Treeview(treeview_frame, columns=(
    '#1', '#2', '#3', '#4', '#5'))
tree.heading('#0', text='No')
tree.column("#0", minwidth=50, width=100)
tree.heading('#1', text='Section')
tree.column("#1", minwidth=50, width=100)
tree.heading('#2', text='Root/Extremum')
tree.column("#2", minwidth=50, width=100)
tree.heading('#3', text='F(x)')
tree.column("#3", minwidth=50, width=100)
tree.heading('#4', text='No. Iter')
tree.column("#4", minwidth=50, width=100)
tree.heading('#5', text='Error')
tree.column("#5", minwidth=50, width=100)
tree.grid(sticky='nsew')

if __name__ == '__main__':
    mainloop()
