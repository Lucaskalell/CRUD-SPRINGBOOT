import pandas as pd
import random

class ServicoLogistica:
    def __init__(self):
        self.dados_remessas = pd.DataFrame(columns=['Codigo', 'Origem', 'Destino', 'Peso', 'Custo'])

    def calcular_custo_frete(self, origem, destino, peso):
        distancia = 200  # Simulação de uma distância fixa em km
        custo_pedagio = 50  # Simulação de custo de pedágio fixo em $
        custo = distancia * 0.1 + peso * 0.5 + custo_pedagio
        codigo = random.randint(1000, 9999)
        self.dados_remessas = self.dados_remessas.append({'Codigo': codigo, 'Origem': origem, 'Destino': destino, 'Peso': peso, 'Custo': custo}, ignore_index=True)
        return custo

    def salvar_dados_remessas(self, filename):
        self.dados_remessas.to_csv(filename, index=False)

    def carregar_dados_remessas(self, filename):
        self.dados_remessas = pd.read_csv(filename)

def main():
    servico = ServicoLogistica()

    origem = "São Paulo"
    destino = "Rio de Janeiro"
    peso = 500

    custo_total = servico.calcular_custo_frete(origem, destino, peso)
    print("O custo total do frete é: $", custo_total)

    servico.salvar_dados_remessas("dados_remessas.csv")

    servico.carregar_dados_remessas("dados_remessas.csv")
    print("Dados de remessas carregados:")
    print(servico.dados_remessas)


if __name__ == "__main__":
    main()
