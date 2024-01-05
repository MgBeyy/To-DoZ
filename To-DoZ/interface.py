from customtkinter import *  #Tkinter modülünün özelleştirilmiş hali
from tkinter import Listbox
from function import *  
import os
from PIL import Image

# Yeni bir görev eklemek için kullanılacak fonksiyon
def add_function():
    name = name_entry.get()
    date = date_entry.get()
    if name == "":
        error_label.configure(text="Task name cannot be empty.\n Please enter a valid task name.")
    add_task(name, date)
    show_tasks()

# Bir görevi kaldırmak için kullanılacak fonksiyon
def remove_function():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task_id = int(task_listbox.get(selected_task_index).split(":")[0])
        remove_task(selected_task_id)
        show_tasks()
    else:
        error_label.configure(text="Select a task to remove.")

# Bir görevi tamamlandı olarak işaretlemek için kullanılacak fonksiyon
def done_function():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task_id = int(task_listbox.get(selected_task_index).split(":")[0])
        mark_done(selected_task_id)
        show_tasks()
    else:
        error_label.configure(text="Select a task to mark as done.")

# Görev listesini gösteren fonksiyon
def show_tasks():
    task_listbox.delete(0, END)
    conn = sqlite3.connect('To-DoZ.db')  # To-Do uygulamasının veritabanına bağlan
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        if len(row) == 4:
            id, name, date, isDone = row
            if isDone:
                task_listbox.insert(END, f"{id}: {name} {date} Done")
            else:
                task_listbox.insert(END, f"{id}: {name} {date} Not done")
        else:
            print("Invalid row format::", row)

# Veritabanı tablosunu oluştur
create_table()

# Arayüz temasını koyu moda ayarla
set_appearance_mode('dark')

# Renk temasını belirle
set_default_color_theme('black-yellow.json')

# Uygulamanın penceresini oluştur
app = CTk()
app.title("To-DoZ")
app.geometry("405x720")

# To-DoZ logosunun dosya yolu
logo_path = os.path.join(os.path.dirname(__file__), 'Images/to-doz.png')

# To-DoZ logosunu yükleyip görüntüle
logo = CTkImage(dark_image=Image.open(logo_path), size=(150, 150))
logo_label = CTkLabel(app, image=logo, text="")
logo_label.grid(columnspan=2, padx=127, pady=40)

# İkon dosyalarının dosya yolları
add_icon_path = os.path.join(os.path.dirname(__file__), 'Images/plus_icon.png')
done_icon_path = os.path.join(os.path.dirname(__file__), 'Images/tick_icon.png')
remove_icon_path = os.path.join(os.path.dirname(__file__), 'Images/trash_icon.png')

# İkonları yükleyip görüntüle
add_icon = CTkImage(dark_image=Image.open(add_icon_path), size=(20, 20))
done_icon = CTkImage(dark_image=Image.open(done_icon_path), size=(20, 20))
remove_icon = CTkImage(dark_image=Image.open(remove_icon_path), size=(20, 20))

# Arayüzdeki etiketler, giriş kutuları ve düğmeler
name_label = CTkLabel(app, text="Task Name:")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = CTkEntry(app)
name_entry.grid(row=1, column=1, padx=10, pady=10)

date_label = CTkLabel(app, text="Task Date:")
date_label.grid(row=2, column=0, padx=10, pady=10)
date_entry = CTkEntry(app)
date_entry.grid(row=2, column=1, padx=10, pady=10)

add_button = CTkButton(app, text="Add Task", image=add_icon, command=add_function)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

task_listbox = Listbox(app, height=10, width=50)
task_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

show_tasks()

mark_done_button = CTkButton(app, text="Mark as Done", image=done_icon, command=done_function)
mark_done_button.grid(row=5, column=1, pady=10)

remove_button = CTkButton(app, text="Remove Task", image=remove_icon, command=remove_function)
remove_button.grid(row=5, column=0, pady=10)

error_label = CTkLabel(app, text="", text_color='red', font=('Roboto', 20))
error_label.grid(row=6, columnspan=2, padx=10, pady=10)

app.mainloop()
