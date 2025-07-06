"""Módulo Cálculo do NPS - Net Promoter Score

O NPS é uma métrica utilizada para medir a lealdade e 
satisfação dos clientes em relação a uma empresa. 
Ele é calculado através de uma pesquisa que pergunta aos clientes o quão provável
é que eles recomendem a empresa a amigos ou colegas. 
Os clientes são classificados em três categorias: promotores, passivos e detratores. 
O NPS é importante porque ajuda as empresas a identificar áreas de melhoria e a otimizar
a experiência do cliente, promovendo um crescimento sustentável.
"""
class Nps:
    """Representa o NPS - pode ser utilizado por um sistema de avaliação da qualidade de um serviço.
    
    Atributos:
        notas (list): lista de notas,com valores de 0 a 10, que compõe o cálculo de um NPS.
    """
    def __init__(self) -> None:
        """Inicializa uma nova instância da classe Nps
        """
        self.notas = []

    def validar_nota(func) -> None:
        """Função decorator para validar o valor da nota
        """
        def wrapper(self, nota):
            if 0 <= nota <= 10:
                func(self, nota)
            else:
                print('A nota deve ter um valor entre 0 e 10')
        return wrapper

    @validar_nota
    def adicionar_nota(self, nota):
        """Adiciona uma nota na lista de notas para o cálculo do NPS"""
        self.notas.append(nota)

    def calcular_nps(self) -> float:
        """Realiza o cáculo do NPS:
            Partindo da pontuação de 0 a 10, atribuida pelos respondentes de uma pesquisa, 
            eles são classificados em três diferentes níveis:
            Promotores: atribuem nota 9 ou 10, revelando altas chances de recomendar sua empresa
            Neutros: dão nota 7 ou 8. Sua relação com a companhia é regular, mas existem pontos 
            a melhorar; 
            Detratores: nota de 0 a 6. Estão descontentes com seu produto, serviço ou atendimento, 
            o que pode levá-los a fazer uma propaganda negativa.
            
            Fórmula de cáculo:
            % detratores = quantidade de respostas com nota <= 6 / total de notas * 100
            % promotores = quantidade de respostas com nota >= 9 / total de notas * 100
            nps = % promotores - % detratoress

            Retorna o valor do nps.
        """
        detratores = [n for n in self.notas if n <= 6]
        promotores = [n for n in self.notas if n >= 9]

        percent_detratores = (len(detratores)/ len(self.notas)) * 100
        percent_promotores = (len(promotores)/ len(self.notas)) * 100

        nps = percent_promotores - percent_detratores
        return nps

    def avaliar_classificacao(self):
        """Classsifica o resultado do NPS
        """
        nps = self.calcular_nps()
        if nps < 0:
            print('Zona Crítica')
        elif nps < 50:
            print('Zona Neutra (Razoável)')
        elif nps < 75:
            print('Zona de Qualidade (Muito bom)')
        else:
            print('Zona de Excelência (Excelente)')

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

    print(f'Valor do NPS = {enquete1.calcular_nps()}')
    enquete1.avaliar_classificacao()
