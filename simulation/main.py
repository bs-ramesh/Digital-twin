from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

my_w = tk.Tk()
my_w.geometry("1560x800")  # Size of the window 
my_w.title("DIGITAL TWIN")  # Adding a title
my_w.bind('<Escape>', lambda e:my_w.quit()) # to close.
my_w.state('zoomed')

label_frame1 = LabelFrame(my_w, text='label frame 1', width=600, height=400)
label_frame1.pack(expand='yes', fill='both')

label1 = Label(label_frame1, text='')
label1.place(x=0, y=5)

label2 = Label(label_frame1, text='')
label2.place(x=0, y=35)

label3 = Label(label_frame1, text='')
label3.place(x=0, y=65)

label_frame11 = LabelFrame(my_w, text='label frame 1.1', width=500, height=200)
label_frame11.place(relx=1.0, rely=0.0, anchor='ne')  # This places it in the top-right corner

button_simulate = Button(label_frame11, text='Simulate',bg='blue', fg='white')
button_simulate.place(relx=0.5, rely=0.5, anchor='center')

label_time = Label(label_frame11, text='Time in seconds:')
label_time.place(relx=0.38, rely=0.35, anchor='center')

entry_time = Entry(label_frame11)
entry_time.place(relx=0.47, rely=0.3)

label_frame2 = LabelFrame(my_w, width=30, height=30)
label_frame2.pack(expand='yes', fill='both')

label_frame12 = LabelFrame(my_w, width=500, height=200)
label_frame12.place(relx=0.6745, rely=0.25)  # This places it in the bottom-right corner

label_frame21 = LabelFrame(my_w, width=600, height=212)
label_frame21.place(relx=0.02, rely=0.95, anchor='sw')  # This places it in the bottom-left corner

label_devices = Label(label_frame2, text='Number of Devices:')
label_devices.place(relx=0.010, rely=0.2)

entry = Entry(label_frame2)
entry.place(relx=0.082, rely=0.2)

button_update = Button(label_frame2, text='Submit')
button_update.place(relx=0.165, rely=0.19)

# Load and display images
image_filenames = ["simulation/car.png", "simulation/smart-watch.png", "simulation/television.png", "simulation/laptop.png"]
for idx, image_filename in enumerate(image_filenames):
    img = Image.open(image_filename)
    img = img.resize((50, 50), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    label = Label(label_frame21, image=photo)
    label.image = photo  # Keep a reference to prevent garbage collection
    label.grid(row=0, column=idx, padx=10, pady=10)

# Add label_frame22 and elements inside
label_frame22 = LabelFrame(label_frame12, text='Configuration', width=300, height=200)
label_frame22.place(relx=0.7, rely=0.8, anchor='se')  # This places it in the bottom-right corner

label_device_id = Label(label_frame22, text='Device ID:')
label_device_id.grid(row=0, column=0, padx=5, pady=5, sticky='w')

entry_device_id = Entry(label_frame22,state='readonly')
entry_device_id.grid(row=0, column=1, padx=5, pady=5)

label_device_type = Label(label_frame22, text='Device Type:')
label_device_type.grid(row=1, column=0, padx=5, pady=5, sticky='w')

entry_device_type = Entry(label_frame22,state='readonly')
entry_device_type.grid(row=1, column=1, padx=5, pady=5)

label_device_name = Label(label_frame22, text='Device Name:')
label_device_name.grid(row=2, column=0, padx=5, pady=5, sticky='w')

entry_device_name = Entry(label_frame22,state='readonly')
entry_device_name.grid(row=2, column=1, padx=5, pady=5)

label_model = Label(label_frame22, text='Model:')
label_model.grid(row=3, column=0, padx=5, pady=5, sticky='w')

entry_model = Entry(label_frame22,state='readonly')
entry_model.grid(row=3, column=1, padx=5, pady=5)

my_w.mainloop()  # Keep the window open

