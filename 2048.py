import sys,os,random,itertools


class Game:
    grid = []
    controls = ['w','a','s','d']

    def rnd_field(self):
        number = random.choice([4,2,4,2,4,2,4,2,4,2,4,2])
        itertools.product([0,1,2,3],[0,1,2,3])

    def print_screen(self):
        os.system('clear')
        print('-' * 30)
        for row in self.grid:
           print('|{}|'.format( "|".join([str(col or " ").center(4) for col in row])))
           print('-' * 21)

    def logic(self,control):
        return 0,""

    def main_loop(self):
        self.grid = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
        self.rnd_field()
        self.rnd_field()
        while True:
            self.print_screen()
            control = input('input w/a/s/d:')
            if control in self.controls:
                status,info = self.logic(control)
                if status:
                    print(info)
                    if input('Start another game?[Y/n]'.lower()) == "y":
                        break
                    else:
                        sys.exit(0)

        self.main_loop()

if __name__ == '__main__':
    Game().main_loop()
