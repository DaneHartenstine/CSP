# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    url_val = url_val.replace(" ", "")
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

# Save function.
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()



root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("Retro Search")


root.configure(background="black")

ping_img = tk.PhotoImage(file="spaceinvaders.gif")
ping_img = ping_img.subsample(5,5)

# set up button to run the do_command function
# Modifies the ping button parameters.
ping_btn = tk.Button(frame, text="ping", 
    command=lambda:do_command("ping -c 10"),
    image=ping_img)
ping_btn.pack(side=tk.LEFT) 

lookup_image = tk.PhotoImage(file="ghost.gif")
lookup_image = lookup_image.subsample(1,1)

NSlookup_btn = tk.Button(frame, text="NSlookup", 
    command=lambda:do_command("NSlookup"),
    image=lookup_image)
NSlookup_btn.pack(side=tk.LEFT)

tr_img = tk.PhotoImage(file="mario.gif")
tr_img = tr_img.subsample(5,5)

traceroot_btn = tk.Button(frame, text="Traceroot", 
    command=lambda:do_command("dig +trace"),
    image=tr_img)
traceroot_btn.pack(side=tk.LEFT)

pac_img = tk.PhotoImage(file="pacman.gif")
pac_img = pac_img.subsample(3,3)

save_btn = tk.Button(frame, text="Save", 
    command=lambda:mSave(),
    image=pac_img)
save_btn.pack(side=tk.LEFT)

ping_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
ping_URL.pack()

ping_label = tk.Label(ping_URL, text="Ping             ",
    compound="center",
    font=("comic sans", 14),
    bd=0,
    fg="green2",
    bg="black")
ping_label.pack(side=tk.LEFT)

ns_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
ns_URL.pack()

ns_label = tk.Label(ping_URL, text="NSLookup                ",
    compound="center",
    font=("comic sans", 14),
    bd=0,
    fg="green2",
    bg="black")
ns_label.pack(side=tk.LEFT)

trc_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
trc_URL.pack()

trc_label = tk.Label(ping_URL, text="Traceroot            ",
    compound="center",
    font=("comic sans", 14),
    bd=0,
    fg="green2",
    bg="black")
trc_label.pack(side=tk.LEFT)

save_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
save_URL.pack()

save_label = tk.Label(ping_URL, text="Save",
    compound="center",
    font=("comic sans", 14),
    bd=0,
    fg="green2",
    bg="black")
save_label.pack(side=tk.RIGHT)


# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    fg="green2",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame,bg="black", fg="green2", height=10, width=100)
command_textbox.pack()



root.mainloop()
