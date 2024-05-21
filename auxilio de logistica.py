import random

class ServicoLogistica:
    def __init__(self):
        self.dados_remessas = []

    def calcular_custo_frete(self, origem, destino, peso):
        distancia = 844  # Simulação de uma distância fixa em km
        custo_pedagio = 91.20 # Simulação de custo de pedágio fixo em $
        custo = distancia * 0.5 + peso * 10 + custo_pedagio
        codigo = random.randint(1000, 9999)
        nova_remessa = {'Codigo': codigo, 'Origem': origem, 'Destino': destino, 'Peso': peso, 'Custo': custo}
        self.dados_remessas.append(nova_remessa)
        return custo

    def salvar_dados_remessas(self, filename):
        with open(filename, 'w') as file:
            for remessa in self.dados_remessas:
                file.write(f"{remessa['Codigo']},{remessa['Origem']},{remessa['Destino']},{remessa['Peso']},{remessa['Custo']}\n")

    def carregar_dados_remessas(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                codigo, origem, destino, peso, custo = line.strip().split(',')
                self.dados_remessas.append({'Codigo': int(codigo), 'Origem': origem, 'Destino': destino, 'Peso': float(peso), 'Custo': float(custo)})

def main():
    servico = ServicoLogistica()

    origem = "São Paulo"
    destino = "Santa catarina"
    peso = 754

    custo_total = servico.calcular_custo_frete(origem, destino, peso)
    print("O custo total do frete é: $", custo_total)

    servico.salvar_dados_remessas("dados_remessas.csv")

    servico.carregar_dados_remessas("dados_remessas.csv")
    print("Dados de remessas carregados:")
    for remessa in servico.dados_remessas:
        print(remessa)


if __name__ == "__main__":
    main()
