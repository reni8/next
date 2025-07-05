class Nps:
    def __init__(self):
        self.notas = [] 

    def adicionar_nota(self, nota):
        if 0 <= nota <=10:
            self.notas.append(nota)
        else:
            print('A nota deve ter um valor entre 0 e 10')
    
    def calcular_nps(self):
        detratores = [n for n in self.notas if n <= 6]
        promotores = [n for n in self.notas if n >= 9]

        percent_detratores = (len(detratores)/ len(self.notas)) * 100
        percent_promotores = (len(promotores)/ len(self.notas)) * 100

        nps = percent_promotores - percent_detratores
        return nps

if __name__ == '__main__':
    enquete1 = Nps()
    
    enquete1.adicionar_nota(10)
    enquete1.adicionar_nota(9)
    enquete1.adicionar_nota(9)
    enquete1.adicionar_nota(8)
    enquete1.adicionar_nota(5)
    enquete1.adicionar_nota(9)
    enquete1.adicionar_nota(5)
    enquete1.adicionar_nota(7)
    enquete1.adicionar_nota(10)
    enquete1.adicionar_nota(9)
    enquete1.adicionar_nota(10)

    print(enquete1.calcular_nps())
