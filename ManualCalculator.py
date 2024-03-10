import tkinter as tk
# Function to evaluate the expression
def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to append characters to the entry
def append_character(char):
    entry.insert(tk.END, char)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(background="pink")
root.geometry("300x500")
# Create StringVar to store the result
result = tk.StringVar()

# Entry to display and input the expression
entry = tk.Entry(root, textvariable=result, font=('Helvetica', 20), bd=10,  justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


#button 7
button = tk.Button(root, text="7", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="7": append_character(char))
button.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

#button 8
button = tk.Button(root, text="8", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="8": append_character(char))
button.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

#button 9
button = tk.Button(root, text="9", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="9": append_character(char))
button.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

#button *
button = tk.Button(root, text="*", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="*": append_character(char))
button.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")


#button 6
button = tk.Button(root, text="6", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="6": append_character(char))
button.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")


#button 5
button = tk.Button(root, text="5", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="5": append_character(char))
button.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")


#button 4
button = tk.Button(root, text="4", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="4": append_character(char))
button.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

#button *
button = tk.Button(root, text="/", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="/": append_character(char))
button.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")



#button 3
button = tk.Button(root, text="3", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="3": append_character(char))
button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")


#button 2
button = tk.Button(root, text="2", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="2": append_character(char))
button.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")


#button 1
button = tk.Button(root, text="1", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="1": append_character(char))
button.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")


#button -
button = tk.Button(root, text="-", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="-": append_character(char))
button.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

#button 0
button = tk.Button(root, text="0", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="0": append_character(char))
button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

#button .
button = tk.Button(root, text=".", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char=".": append_character(char))
button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

#button c
button = tk.Button(root, text="C", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=clear_entry)
button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

#button +
button = tk.Button(root, text="+", fg='black', bg='white', font=('Helvetica', 20), padx=20, pady=10,
                       command=lambda char="+": append_character(char))
button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

# Evaluate Button
eval_button = tk.Button(root, text='=', fg='black', bg='white',font=('Helvetica', 20), padx=20, pady=10,
                        command=evaluate_expression)
eval_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Configure row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the main event loop
root.mainloop()


