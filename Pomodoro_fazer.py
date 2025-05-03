# Escolher tempos
# Mostrar tempo total trabalhado
# Mostrar tempo por disciplina
# Matplotlib para guardar tempo trabalhado ao longo de dias, etc.
# Guardar Dados que duram depois de fechar o programa
# Colocar alarme para fim do tempo
import tkinter as tk
from ttkbootstrap import ttk, Style


class Pomodoro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Pomodoro Timer")

        self.style = Style(theme="morph")
        self.style.theme_use()

        self.temporizador = tk.Label(
            self.root, text='20:00', font=('Arial', 80))
        self.temporizador.pack(pady=5)

        self.start_button = ttk.Button(
            self.root, text="Iniciar tempo", command=self.Iniciar_tempo)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(
            self.root, text="Parar tempo", command=self.Parar_tempo, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.temporizador_ativo = True
        self.tempo_de_trabalho = 2
        self.tempo_de_pausa_curta = 5

        self.pausa = False

        self.tempo_atual = self.tempo_de_trabalho

        self.root.mainloop()

    def Parar_tempo(self):
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.temporizador_ativo = False

    def Atualizar_tempo(self):
        if self.tempo_atual <= 0:
            self.Parar_tempo()
            self.Fim_de_tempo()
        if self.temporizador_ativo:
            self.tempo_atual -= 1
            minutos = self.tempo_atual//60
            segundos = self.tempo_atual-minutos*60
            self.temporizador.config(text='{0}:{1}'.format(
                minutos, segundos), font=('Arial', 80))
            self.root.after(1000, self.Atualizar_tempo)

    def Iniciar_tempo(self):
        self.temporizador_ativo = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.Atualizar_tempo()

    def Fim_de_tempo(self):
        if self.pausa:
            self.pausa = False
            self.temporizador.config(
                text='Hora de trabalhar!', font=('Arial', 40))

        else:
            self.pausa = True
            self.temporizador.config(text='Hora da pausa!', font=('Arial', 40))
            self.tempo_atual = self.tempo_de_pausa_curta


Pomodoro()
