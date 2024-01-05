import sqlite3


# Görevleri tutmak için "Task" adında bir sınıf oluştur.
class Task:
    def __init__(self, id, name, date, isDone=False):
        self.id = id
        self.name = name
        self.date = date
        self.isDone = isDone

# Veritabanında "tasks" tablosunu oluşturur.
def create_table():
    conn = sqlite3.connect('To-DoZ.db')  # To-DoZ uygulamasının veritabanına bağlan
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, isDone INTEGER)''')  # Eğer yoksa "tasks" tablosunu oluştur
    conn.commit()  # Veritabanındaki değişiklikleri kaydet
    conn.close()  # Bağlantıyı kapat

# Yeni bir görev ekler
def add_task(name, date):
    task = Task(None, name, date)  # Task sınıfından bir örnek oluştur
    conn = sqlite3.connect('To-DoZ.db')  # To-DoZ uygulamasının veritabanına bağlan
    c = conn.cursor()
    c.execute("INSERT INTO tasks (name, date, isDone) VALUES (?, ?, ?)", (task.name, task.date, task.isDone))  # Görevi veritabanına ekle
    conn.commit()  # Veritabanındaki değişiklikleri kaydet
    conn.close()  # Bağlantıyı kapat

# Belirli bir görevi kaldırır
def remove_task(task_id):
    conn = sqlite3.connect('To-DoZ.db')  # To-DoZ uygulamasının veritabanına bağlan
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))  # Belirli bir görevi ID'ye göre kaldır
    conn.commit()  # Veritabanındaki değişiklikleri kaydet
    conn.close()  # Bağlantıyı kapat

# Belirli bir görevi tamamlandı olarak işaretler
def mark_done(task_id):
    conn = sqlite3.connect('To-DoZ.db')  # To-DoZ uygulamasının veritabanına bağlan
    c = conn.cursor()
    c.execute("UPDATE tasks SET isDone=1 WHERE id=?", (task_id,))  # Belirli bir görevi ID'ye göre tamamlandı olarak işaretle
    conn.commit()  # Veritabanındaki değişiklikleri kaydet
    conn.close()  # Bağlantıyı kapat
