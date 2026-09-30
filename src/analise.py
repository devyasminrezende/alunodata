def validar_aluno(aluno):
    """Verifica se o registro possui os campos obrigatórios."""

    campos_obrigatorios = [
        "matricula",
        "nome",
        "idade",
        "curso",
        "cidade"
    ]

    for campo in campos_obrigatorios:
        if campo not in aluno:
            return False

        if str(aluno[campo]).strip() == "":
            return False

    if not isinstance(aluno["matricula"], int):
        return False

    if not isinstance(aluno["idade"], int) or aluno["idade"] <= 0:
        return False

    return True


def limpar_dados(alunos):
    """Remove registros inválidos e padroniza os textos."""

    dados_limpos = []

    for aluno in alunos:

        if not validar_aluno(aluno):
            continue

        aluno["nome"] = aluno["nome"].strip().title()
        aluno["curso"] = aluno["curso"].strip().title()
        aluno["cidade"] = aluno["cidade"].strip().title()

        dados_limpos.append(aluno)

    return dados_limpos


def encontrar_duplicidades(alunos):
    """Identifica matrículas duplicadas."""

    matriculas = set()
    duplicadas = set()

    for aluno in alunos:

        matricula = aluno["matricula"]

        if matricula in matriculas:
            duplicadas.add(matricula)
        else:
            matriculas.add(matricula)

    return duplicadas


def calcular_idade_media(alunos):
    """Calcula a idade média dos alunos."""

    if not alunos:
        return 0

    soma_idades = sum(aluno["idade"] for aluno in alunos)

    return soma_idades / len(alunos)


def alunos_por_curso(alunos):
    """Conta quantos alunos existem em cada curso."""

    resultado = {}

    for aluno in alunos:

        curso = aluno["curso"]

        if curso not in resultado:
            resultado[curso] = 0

        resultado[curso] += 1

    return resultado


def alunos_por_cidade(alunos):
    """Conta quantos alunos existem em cada cidade."""

    resultado = {}

    for aluno in alunos:

        cidade = aluno["cidade"]

        if cidade not in resultado:
            resultado[cidade] = 0

        resultado[cidade] += 1

    return resultado


def gerar_relatorio(alunos):
    """Gera um relatório resumido dos dados."""

    if not alunos:
        print("\nNenhum dado disponível para análise.")
        return

    idade_media = calcular_idade_media(alunos)
    cursos = alunos_por_curso(alunos)
    cidades = alunos_por_cidade(alunos)

    print("\n" + "=" * 50)
    print("RELATÓRIO DE ANÁLISE DOS DADOS")
    print("=" * 50)

    print(f"Total de alunos: {len(alunos)}")
    print(f"Idade média: {idade_media:.2f} anos")

    print("\nAlunos por curso:")

    for curso, quantidade in cursos.items():
        print(f"- {curso}: {quantidade}")

    print("\nAlunos por cidade:")

    for cidade, quantidade in cidades.items():
        print(f"- {cidade}: {quantidade}")

    print("=" * 50)