class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class GerenciadorFuncionarios:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"Nome: {funcionario.nome}, Cargo: {funcionario.cargo}, Salário: {funcionario.salario}")

def main():
    gerenciador = GerenciadorFuncionarios()

    # Adicionando funcionários
    gerenciador.adicionar_funcionario(Funcionario("Lucas", "Desenvolvedor", 5000))
    gerenciador.adicionar_funcionario(Funcionario("Maria", "Gerente de Projetos", 7000))
    gerenciador.adicionar_funcionario(Funcionario("Pedro", "Analista de Dados", 6000))

    # Listando funcionários
    gerenciador.listar_funcionarios()

if __name__ == "__main__":
    main()