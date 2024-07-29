import tkinter as tk
import random
import string

def generate_password():
    length= int(length_entry.get())
    if length<4:
        password_label.config(text="Password length should be at least 4")
        return

    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=f"Generated Password: {password}",bg="Yellow",fg="black",font=("comic sans ms",15))

#create the main window
root=tk.Tk()
root.title("Password Generator")
root.geometry("420x500+200+200")

#create a lable for the length input
length_label=tk.Label(root,text="Enter password length (min 4):",font=("comic sans ms",15))
length_label.pack()

#create an entry for the password length
length_entry=tk.Entry(root)
length_entry.pack()

#create a button to generate the password
generate_button=tk.Button(root,text="Generate Password",font=("comic sans ms",15),command= generate_password)
generate_button.config(bg="light yellow",fg="black")
generate_button.pack()


#create a label to display the generated password
password_label=tk.Label(root,text="")
password_label.pack()

#Run the application/code
root.mainloop()





