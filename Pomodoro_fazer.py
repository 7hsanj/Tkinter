# Escolher tempos (FEITO)
# Fazer com que mudar o tempo apenas afete diferença e não dar só set (FEITO?)
# Mostrar tempo total trabalhado (FEITO)

# Outra classe para file handling (FEITO)
# Tempo total no ficheiro (FEITO)
# Mudar variaveis do tempo após fechar (FEITO)

# Tempo por disciplina
# Tempo por dias

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

        # teste = tk.IntVar(self.root, value=15)
        # print(teste.get())

        self.style = Style(theme="morph")
        self.style.theme_use()

        self.intvar_trabalho = tk.IntVar(value=25)
        self.intvar_pausa_curta = tk.IntVar(value=5)
        self.intvar_pausa_longa = tk.IntVar(value=15)

        self.tempo_atual = self.intvar_trabalho.get()*60
        self.minutos = self.tempo_atual//60
        self.segundos = self.tempo_atual-self.minutos*60
        # print(self.tempo_atual)

        self.main = tk.Frame(self.root)
        self.escolher = tk.Frame(self.root)

        self.pausa = False
        self.pomodoro_feitos = 1
        self.temporizador_ativo = False
        self.tempo_passado = 0
        self.tempo_passado_total = 0

        self.Criar_Widgets()
        self.Tempo_escolhido_trabalho()
        self.Tempo_escolhido_curta()
        self.Tempo_escolhido_longa()

        self.intvar_trabalho.trace_add('write', self.Tempo_escolhido_trabalho)
        self.intvar_pausa_curta.trace_add('write', self.Tempo_escolhido_curta)
        self.intvar_pausa_longa.trace_add('write', self.Tempo_escolhido_longa)

        self.main.pack()

        self.root.mainloop()

    def Criar_Widgets(self):
        # Main
        self.temporizador = tk.Label(
            self.main, text='{0}:{1}'.format(self.minutos, self.segundos), font=('Arial', 80))
        self.temporizador.pack(pady=5)

        self.start_button = ttk.Button(
            self.main, text="Iniciar tempo", command=self.Iniciar_tempo)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(
            self.main, text="Parar tempo", command=self.Parar_tempo, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.choose_button = ttk.Button(
            self.root, text='Escolher tempo', command=self.Escolher_tempo)
        self.choose_button.place(relx=0.8, rely=0.9, anchor='center')

        # Tempo Total
        self.tempo_passado_anterior = FileHandling().Reading()

        self.tempo_total = tk.Label(
            self.root, text='Tempo total trabalhado: {0} minutos'.format(self.tempo_passado_anterior), font=('Arial', 10))
        self.tempo_total.place(relx=0.3, rely=0.9, anchor='center')

        # Escolhas
        self.label_escolher = tk.Label(
            self.escolher, text='Personaliza os teus tempos!', font=('Arial', 20))
        self.label_escolher.pack(pady=5)

        self.titulo_trabalho = tk.Label(
            self.escolher, text='Tempo de Trabalho', font=('Arial', 10))
        self.titulo_trabalho.pack(pady=5)

        self.entry_tempo_de_trabalho = tk.Entry(
            self.escolher, textvariable=self.intvar_trabalho)
        self.entry_tempo_de_trabalho.pack()

        self.titulo_curta = tk.Label(
            self.escolher, text='Tempo da Pausa', font=('Arial', 10))
        self.titulo_curta.pack(pady=5)

        self.entry_tempo_de_pausa_curta = tk.Entry(
            self.escolher, textvariable=self.intvar_pausa_curta)
        self.entry_tempo_de_pausa_curta.pack()

        self.titulo_longa = tk.Label(
            self.escolher, text='Tempo da Grande Pausa', font=('Arial', 10))
        self.titulo_longa.pack(pady=5)

        self.entry_tempo_de_pausa_longa = tk.Entry(
            self.escolher, textvariable=self.intvar_pausa_longa)
        self.entry_tempo_de_pausa_longa.pack()

        self.back_button = ttk.Button(
            self.root, text='Voltar', command=self.Voltar_Pomodoro)

    def Escolher_tempo(self):
        self.main.pack_forget()
        self.choose_button.place_forget()
        self.back_button.place(relx=0.8, rely=0.9, anchor='center')
        self.temporizador_ativo_antes = self.temporizador_ativo
        self.Parar_tempo()

        self.escolher.pack()

    def Voltar_Pomodoro(self):
        self.main.pack()
        self.escolher.pack_forget()
        self.back_button.place_forget()
        self.choose_button.place(relx=0.8, rely=0.9, anchor='center')
        if self.temporizador_ativo_antes == True:
            self.Iniciar_tempo()

    def Tempo_escolhido_trabalho(self, *args):
        self.tempo_de_trabalho = self.intvar_trabalho.get()*60
        if not self.pausa:
            self.tempo_atual = self.tempo_de_trabalho-self.tempo_passado
        self.Mostrar_tempo()

    def Tempo_escolhido_curta(self, *args):
        self.tempo_de_pausa_curta = self.intvar_pausa_curta.get()*60
        if self.pausa and not self.pomodoro_feitos == 4:
            self.tempo_atual = self.tempo_de_pausa_curta-self.tempo_passado
        self.Mostrar_tempo()

    def Tempo_escolhido_longa(self, *args):
        self.tempo_de_pausa_longa = self.intvar_pausa_longa.get()*60
        if self.pausa and self.pomodoro_feitos == 1:
            self.tempo_atual = self.tempo_de_pausa_longa-self.tempo_passado
        self.Mostrar_tempo()

    def Mostrar_tempo(self):
        self.minutos = self.tempo_atual//60
        self.segundos = self.tempo_atual-self.minutos*60
        self.temporizador.config(text='{0}:{1}'.format(
            self.minutos, self.segundos), font=('Arial', 80))

    def Parar_tempo(self):
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.temporizador_ativo = False

    def Iniciar_tempo(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.temporizador_ativo = True
        self.Atualizar_tempo()

    def Atualizar_tempo(self):
        if self.tempo_atual <= 0:
            self.Parar_tempo()
            self.Fim_de_tempo()
        if self.temporizador_ativo:
            self.tempo_atual -= 1
            self.tempo_passado += 1
            if not self.pausa:
                global tempo_passado_file
                tempo_passado_file = self.tempo_passado
            # print(self.tempo_passado)
            self.Mostrar_tempo()
            self.root.after(1, self.Atualizar_tempo)

    def Fim_de_tempo(self):
        if self.pausa:
            self.tempo_passado = 0
            self.pausa = False
            self.temporizador.config(
                text='Hora de trabalhar!', font=('Arial', 35))
            self.tempo_atual = self.tempo_de_trabalho
        else:
            self.pausa = True
            self.tempo_passado_total += self.tempo_passado
            global tempo_passado_total_file
            tempo_passado_total_file = self.tempo_passado_total
            self.tempo_passado = 0
            global tempo_passado_file
            tempo_passado_file = self.tempo_passado
            self.tempo_total.config(
                text='Tempo total trabalhado: {0} minutos'.format(self.tempo_passado_anterior+self.tempo_passado_total//60))
            if self.pomodoro_feitos == 4:
                self.temporizador.config(
                    text='Hora de uma grande pausa!', font=('Arial', 20))
                self.tempo_atual = self.tempo_de_pausa_longa
                self.pomodoro_feitos = 1
            else:
                self.temporizador.config(
                    text='Hora da pausa!', font=('Arial', 40))
                self.tempo_atual = self.tempo_de_pausa_curta
                self.pomodoro_feitos += 1
        print(self.pomodoro_feitos)


class FileHandling:
    def Closing(self):
        try:
            self.ficheiro = open('tempos.txt', 'x')
        except FileExistsError:
            pass
        self.ficheiro = open('tempos.txt', 'a')
        try:
            self.tempo_total = tempo_passado_total_file//60+tempo_passado_file//60
        except:
            self.tempo_total = tempo_passado_file//60
        self.ficheiro.write(str(self.tempo_total)+'\n')

    def Reading(self):
        self.ficheiro = open('tempos.txt', 'r')
        self.tempos = self.ficheiro.read().splitlines()
        self.soma = 0
        # print(self.tempos)
        for x in self.tempos:
            self.soma += int(x)
        return self.soma


Pomodoro()
FileHandling().Closing()
