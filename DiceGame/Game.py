import os
from User import *


class Game(object):
    def __init__(self):
        self.game_round = 1
        self.computer_points = 0
        self.player_points = 0
        self.player = User()
        self.computer = User()

    def start(self):
        while True:
            option = 0
            os.system("cls")
            print "***************"
            print "**Gra w Kosci**"
            print "***************"
            print "1. Nowa gra"
            print "2. Exit"
            print "***************"
            try:
                option = input("Wybierz opcje: ")
            except (NameError, SyntaxError):
                os.system("cls")
                print "Sprobuj ponownie. [1, 2]\n"
            if option == 1:
                self.new_game()
            elif option == 2:
                exit(1)
            else:
                pass

    def new_game(self):
        os.system("cls")
        print "\n*Rozpoczynamy gre*"
        print "Punkty gracz " + str(self.player_points)
        print "Punkty komputera " + str(self.computer_points)
        raw_input("(Wcisnij enter, by zaczac potyczke)")
        while self.game_round <= 13:
            print "---Runda: " + str(self.game_round) + "--------"
            self.player_move()
            self.computer_move()
            self.game_round += 1
            print "\nPunkty gracza: " + str(self.player_points)
            print "Punkty komputera: " + str(self.computer_points)
            print "----------------------------------------------"
        print "Wynik: ",
        if self.player_points > self.computer_points:
            print "Gracz wygrywa z " + str(self.player_points) + " punktami"
        else:
            print "Komputer wygrywa z " + str(self.computer_points) + " punktami"
        raw_input("(Wcisnij enter, by zakonczyc potyczke)\n")
        self.clear_game()

    def clear_game(self):
        self.game_round = 1
        self.computer_points = 0
        self.player_points = 0
        self.player.clear_rules()
        self.computer.clear_rules()

    def player_move(self):
        raw_input("(Wcisnij enter, bu rzucic kostkami)")
        rolls = self.player.first_roll()
        while rolls >= 0:
            answer = 10
            self.player.show_dices()
            self.player.possible_rules()
            print "1. Zabierz kosc ze stolu"
            print "2. Zakoncz runde wyborem punktow"
            if rolls > 0:
                print "3. Rzuc ponownie  " + str(rolls) + "/3"
            try:
                answer = input("Wybor: ")
            except (SyntaxError, NameError, UnboundLocalError):
                print "Nie poprawna wartosc\n"
            if answer == 1:
                self.lock_dice()
            elif answer == 3 and rolls > 0:
                rolls = self.player.roll_dices()
            elif answer == 2:
                rule = raw_input("Podaj regule: ")
                self.player_points += self.player.lock_rule(rule)
                break
        self.player.clear_round()

    def lock_dice(self):
        self.player.show_dices()
        try:
            diceToTake = input("Ktora kostke zabrac?: ")
            if diceToTake in range(0, 7):
                  if not self.player.lock_dice(diceToTake):
                    print "Nie ma takiej kostki\n"
            else:
                  print "Zly zakres\n"
        except (SyntaxError, NameError):
            print "Nie poprawne dane\n"

    def computer_move(self):
        print "Tura komputera......................"
        rolls = self.computer.first_roll()
        roll = random.randint(1, 3)
        best_rule = None
        while rolls >= roll:
            self.computer.show_dices()
            best_rule = self.computer.best_rule()
            if self.computer.get_points_from_rule(best_rule) > 40:
                break
            rolls = self.computer.roll_dices()
        self.computer_points += self.computer.lock_rule(best_rule)
        self.computer.clear_round()
