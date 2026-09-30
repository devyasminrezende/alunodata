import json
from pathlib import Path
from analise import limpar_dados,gerar_relatorio, encontrar_duplicidades

ARQUIVO = Path(__file__).parent.parent / "data" / "alunos.json"


def carregar_alunos():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            if not isinstance(dados, list):
                return []

            return dados

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Aviso: o arquivo de dados está vazio ou corrompido.")
        return []


def salvar_alunos(alunos):
    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)


def gerar_matricula(alunos):
    if not alunos:
        return 1

    matriculas = [
        aluno["matricula"]
        for aluno in alunos
        if isinstance(aluno.get("matricula"), int)
    ]

    return max(matriculas, default=0) + 1


def cadastrar_aluno(alunos):
    print("\n--- CADASTRO DE ALUNO ---")

    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    curso = input("Curso: ").strip()
    cidade = input("Cidade: ").strip()

    aluno = {
        "matricula": gerar_matricula(alunos),
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "cidade": cidade
    }

    alunos.append(aluno)
    salvar_alunos(alunos)

    print(f"\nAluno cadastrado com sucesso!")
    print(f"Matrícula: {aluno['matricula']}")


def listar_alunos(alunos):
    print("\n--- ALUNOS CADASTRADOS ---")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(
            f"Matrícula: {aluno['matricula']} | "
            f"Nome: {aluno['nome']} | "
            f"Idade: {aluno['idade']} | "
            f"Curso: {aluno['curso']} | "
            f"Cidade: {aluno['cidade']}"
        )


def buscar_aluno(alunos):
    print("\n--- BUSCAR ALUNO ---")

    termo = input("Digite o nome ou matrícula: ").strip().lower()

    resultados = []

    for aluno in alunos:
        if (
            termo in aluno["nome"].lower()
            or termo == str(aluno["matricula"])
        ):
            resultados.append(aluno)

    if not resultados:
        print("Nenhum aluno encontrado.")
        return

    for aluno in resultados:
        print(
            f"Matrícula: {aluno['matricula']} | "
            f"Nome: {aluno['nome']} | "
            f"Curso: {aluno['curso']} | "
            f"Cidade: {aluno['cidade']}"
        )


def atualizar_aluno(alunos):
    print("\n--- ATUALIZAR ALUNO ---")

    matricula = int(input("Digite a matrícula do aluno: "))

    for aluno in alunos:
        if aluno["matricula"] == matricula:

            print("Deixe em branco para manter o valor atual.")

            nome = input(f"Nome ({aluno['nome']}): ").strip()
            idade = input(f"Idade ({aluno['idade']}): ").strip()
            curso = input(f"Curso ({aluno['curso']}): ").strip()
            cidade = input(f"Cidade ({aluno['cidade']}): ").strip()

            if nome:
                aluno["nome"] = nome

            if idade:
                aluno["idade"] = int(idade)

            if curso:
                aluno["curso"] = curso

            if cidade:
                aluno["cidade"] = cidade

            salvar_alunos(alunos)

            print("Aluno atualizado com sucesso!")
            return

    print("Aluno não encontrado.")


def excluir_aluno(alunos):
    print("\n--- EXCLUIR ALUNO ---")

    matricula = int(input("Digite a matrícula do aluno: "))

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            salvar_alunos(alunos)

            print("Aluno excluído com sucesso!")
            return

    print("Aluno não encontrado.")


def ordenar_alunos(alunos):
    print("\n--- ORDENAR ALUNOS ---")
    print("1 - Por nome")
    print("2 - Por idade")
    print("3 - Por curso")

    opcao = input("Escolha: ")

    if opcao == "1":
        alunos.sort(key=lambda aluno: aluno["nome"].lower())

    elif opcao == "2":
        alunos.sort(key=lambda aluno: aluno["idade"])

    elif opcao == "3":
        alunos.sort(key=lambda aluno: aluno["curso"].lower())

    else:
        print("Opção inválida.")
        return

    salvar_alunos(alunos)
    print("Alunos ordenados com sucesso!")


def menu():
    alunos = carregar_alunos()

    while True:
        print("\n========== ALUNODATA ==========")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno")
        print("4 - Atualizar aluno")
        print("5 - Excluir aluno")
        print("6 - Ordenar alunos")
        print("7 - Analisar dados")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        try:
            if opcao == "1":
                cadastrar_aluno(alunos)

            elif opcao == "2":
                listar_alunos(alunos)

            elif opcao == "3":
                buscar_aluno(alunos)

            elif opcao == "4":
                atualizar_aluno(alunos)

            elif opcao == "5":
                excluir_aluno(alunos)

            elif opcao == "6":
                ordenar_alunos(alunos)

            elif opcao == "7":
                alunos_limpos = limpar_dados(alunos)

                duplicadas = encontrar_duplicidades(alunos_limpos)

                if duplicadas:
                    print(
                        f"\nMatrículas duplicadas encontradas: {duplicadas}"
                    )

                gerar_relatorio(alunos_limpos)

            elif opcao == "0":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")

        except ValueError:
            print("Erro: digite um valor válido.")


if __name__ == "__main__":
    menu()