import tkinter as tk
from ttkbootstrap import Style
import time

class Clock:
    def __init__(self, master):
        self.master = master
        master.title("Clock")
        global formato
        self.time_label = tk.Label(master, font=("Arial", 80), text="")
        self.time_label.pack(fill=tk.BOTH, expand=True)
        match format_select.get():
            case "H:M:S":
                formato=1
                tempo_at=1
            case "H:M":
                formato=2
                tempo_at=60
            case "H":
                formato=3
                tempo_at=60**2
            case "M:S":
                formato=4
                tempo_at=1
            case _:
                formato=1
                tempo_at=1

        self.update_time()

    def update_time(self):
        global formato
        match formato:
            case 1:
                current_time=time.strftime("%H:%M:%S")
            case 2:
                current_time=time.strftime("%H:%M")
            case 3:
                current_time=time.strftime("%Hh")
            case 4:
                current_time=time.strftime("%M:%S")

        self.time_label.config(text=current_time)
        self.master.after(1000, self.update_time)

def Relogio():
    style = Style()
    #segunda_janela= style.master
    segunda_janela=tk.Toplevel()
    clock = Clock(segunda_janela)
    if mode_select.get()=='Dark':#if int(time.strftime('%H'))>18:
        style.theme_use("cyborg")
    else: style.theme_use('morph')
  
root=tk.Tk()
root.geometry('400x600')

mode_frame=tk.Frame(root)
mode_label=tk.Label(mode_frame,text='Modo do Relógio')
mode_label.pack(pady=5)
mode_select=tk.StringVar(value="Light")
mode= tk.OptionMenu(mode_frame,mode_select,"Light","Dark")
mode.pack(pady=5)
mode_frame.pack(padx=5,pady=5)

format_frame= tk.Frame(root)
format_label=tk.Label(format_frame,text='Formato do Relógio')
format_label.pack(pady=5)
format_select=tk.StringVar(value='H:M:S')
format=tk.OptionMenu(format_frame,format_select,"H:M:S","H:M","H","M:S")
format.pack(pady=5)
format_frame.pack(padx=5,pady=5)

butao=tk.Button(root, text='Inicializar Relógio', command=Relogio)
butao.pack(pady=5)






root.mainloop()