import os
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# classe para representar um aluno
class Aluno:
    def __init__(self, nome, data_nascimento, idioma):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.idioma = idioma

    def __str__(self):
        return f"{self.nome} ({self.data_nascimento}) - {self.idioma}"
        # string ao ser exibida na lista de alunos de um curso

# classe para representar cada curso e suas turmas
class Curso:
    limite_alunos = 20  # cada turma pode ter até 20 alunos
    max_turmas = 2  # cada curso pode ter no máximo 2 turmas

    def __init__(self, idioma):
        self.idioma = idioma
        self.turmas = [[] for _ in range(self.max_turmas)]  # inicializa duas turmas vazias

    def adicionar_aluno(self, aluno):
        for turma in self.turmas:
            if len(turma) < self.limite_alunos:
                turma.append(aluno)
                print(f"\nAluno {aluno.nome} adicionado ao curso de {self.idioma}.")
                return True
        print(f"\nNão há vagas disponíveis para o curso de {self.idioma}.")
        return False

    def listar_alunos(self):
        print(f"\nAlunos do curso de {self.idioma}:")
        for i, turma in enumerate(self.turmas, 1):
            print(f"Turma {i}:")
            if turma:
                for aluno in turma:
                    print(f"  - {aluno}")
            else:
                print("  (Turma vazia)")

# classe principal
class EscolaIdiomas:
    def __init__(self):
        self.cursos = {
            "Inglês": Curso("Inglês"),
            "Espanhol": Curso("Espanhol"),
            "Francês": Curso("Francês")
        }

    def cadastrar_aluno(self, nome, data_nascimento, idioma):
        if idioma in self.cursos:
            if self.validar_data_nascimento(data_nascimento):
                aluno = Aluno(nome, data_nascimento, idioma)
                self.cursos[idioma].adicionar_aluno(aluno)
            else:
                print("Data de nascimento inválida. Use o formato DD/MM/AAAA.")
        else:
            print("Curso inválido. Escolha entre Inglês, Espanhol ou Francês.")

    @staticmethod
    def validar_data_nascimento(data_nascimento):
        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def exibir_alunos(self):
        for curso in self.cursos.values():
            curso.listar_alunos()

if __name__ == "__main__":
    escola = EscolaIdiomas()

    while True:
        print("\nMenu:")
        print("[1] Cadastrar aluno")
        print("[2] Exibir alunos cadastrados")
        print("[0] Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            clear()
            nome = input("Nome do aluno: ")
            data_nascimento = input("\nData de nascimento (DD/MM/AAAA): ")
            idioma = input("\nEscolha um curso (Inglês, Espanhol, Francês): ").capitalize()
            escola.cadastrar_aluno(nome, data_nascimento, idioma)

        elif opcao == "2":
            clear()
            escola.exibir_alunos()

        elif opcao == "0":
            print(" \nSaindo...")
            break
        else:
            clear()
            print("Opção inválida. Tente novamente.")