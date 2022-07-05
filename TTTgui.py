from tkinter import *
from tkinter import messagebox
import random


class TikTakToe():
    def __init__(self):
        self.root = Tk()
        self.root.title('Крестики-нолики')
        self.field = []
        self.game_run = True
        self.cross_count = 0
        self.o_count = 0
        self.win_line = []
        for row in range(10):
            line = []
            for col in range(10):
                button = Button(self.root, text=' ', width=4, height=2, background='violet',
                                command=lambda row=row, col=col: self.click(row, col))
                button.grid(row=row + 2, column=col, sticky="nsew")
                line.append(button)
            self.field.append(line)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.new_button = Button(self.root, text='new game', command=self.new_game)
        self.new_button.grid(row=22, column=0, columnspan=3, sticky='nsew')
        self.root.mainloop()

    def new_game(self):
        for row in range(10):
            for col in range(10):
                self.field[row][col]['text'] = ' '
                self.field[row][col]['background'] = 'violet'
        self.game_run = True
        self.cross_count = 0
        self.o_count = 0

    def check_win(self, r, c, symbol, count=5):
        if not self.check_hor(r, c, symbol, count):
            if not self.check_vert(r, c, symbol, count):
                if not self.check_diag_left(r, c, symbol, count):
                    if not self.check_diag_right(r, c, symbol, count):
                        return
        if symbol == "X":
            text = 'Нолики'
        else:
            text = 'Крестики'
        self.game_run = False
        for el in self.win_line:
            el['background'] = 'red'
        messagebox.showinfo('Победа', f'{text} победили!')

    def check_vert(self, r, c, symbol, n=5):
        count = 0
        self.win_line = []
        for i in range(-4, 5):
            try:
                if self.field[r + i][c]['text'] == symbol:
                    count += 1
                    self.win_line.append(self.field[r + i][c])
                    if count == n:
                        return True
                else:
                    count = 0
                    self.win_line = []
            except IndexError:
                pass
        return False

    def check_hor(self, r, c, symbol, n=5):
        count = 0
        self.win_line = []
        for i in range(-4, 5):
            try:
                if self.field[r][c + i]['text'] == symbol:
                    count += 1
                    self.win_line.append(self.field[r][c + i])
                    if count == n:
                        return True
                else:
                    count = 0
                    self.win_line = []
            except IndexError:
                pass
        return False

    def check_diag_left(self, r, c, symbol, n=5):
        count = 0
        i = -4
        j = 4
        self.win_line = []
        while i < 5 and j > -5:
            try:
                if self.field[r + i][c + j]['text'] == symbol:
                    count += 1
                    self.win_line.append(self.field[r + i][c + j])
                    i += 1
                    j -= 1
                    if count == n:
                        return True
                else:
                    count = 0
                    i += 1
                    j -= 1
                    self.win_line = []
            except IndexError:
                i += 1
                j -= 1
        return False

    def check_diag_right(self, r, c, symbol, n=5):
        count = 0
        i = -4
        j = -4
        self.win_line = []
        while i < 5 and j < 5:
            try:
                if self.field[r + i][c + j]['text'] == symbol:
                    count += 1
                    self.win_line.append(self.field[r + i][c + j])
                    i += 1
                    j += 1
                    if count == n:
                        return True
                else:
                    count = 0
                    i += 1
                    j += 1
                    self.win_line = []
            except IndexError:
                i += 1
                j += 1
        return False

    def computer_move(self):
        symbol = 'O'
        iteration = 0
        while True:
            r = random.randint(0, 9)
            c = random.randint(0, 9)
            iteration += 1
            if self.o_count >=5 :
                if all((self.field[r][c]['text'] == ' ',
                        self.check_hor(r, c, symbol, 4) == False,
                        self.check_vert(r, c, symbol, 4) == False,
                        self.check_diag_left(r, c, symbol, 4) == False,
                        self.check_diag_right(r, c, symbol, 4) == False,
                        iteration < 100 - self.o_count - self.cross_count)):
                    self.field[r][c]['text'] = 'O'
                    self.win_line = []
                    break
                elif iteration == 100 - self.o_count - self.cross_count and self.field[r][c]['text'] == ' ':
                    self.field[r][c]['text'] = 'O'
                break
            else:
                if self.field[r][c]['text'] == ' ':
                    self.field[r][c]['text'] = 'O'
                    break

        return r, c

    def click(self, row, col):
        if self.game_run:
            if self.field[row][col]['text'] == 'X' or self.field[row][col]['text'] == 'O':
                messagebox.showinfo('Проблемка', 'Упс, тут уже занято')
            else:
                self.field[row][col]['text'] = 'X'
                self.cross_count += 1
                if self.cross_count >= 5:
                    self.check_win(row, col, 'X')
                if self.game_run:
                    r, c = self.computer_move()
                    self.o_count += 1
                    if self.o_count >= 5 and self.o_count + self.cross_count < 100:
                        self.check_win(r, c, 'O')
                    elif self.o_count + self.cross_count == 100:
                        messagebox.showinfo('Ничья', "Вот это да! У вас ничья!")


t = TikTakToe()
