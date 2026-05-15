def validar_nota(nota):
    """
    Valida se a nota está no intervalo de 0 a 10.

    Args:
        nota: Nota a validar.

    Returns:
        bool: True se a nota for válida, False caso contrário.
    """
    if not isinstance(nota, (int, float)):
        return False

    return 0 <= nota <= 10


def calcular_media(notas):
    """
    Calcula a média das notas válidas de uma lista.

    Args:
        notas: Lista de notas.

    Returns:
        float: Média das notas válidas.

    Raises:
        ValueError: Se a lista estiver vazia ou se não houver notas válidas.
    """
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")

    notas_validas = [nota for nota in notas if validar_nota(nota)]

    if not notas_validas:
        raise ValueError("Não há notas válidas para calcular a média.")

    return sum(notas_validas) / len(notas_validas)


def obter_situacao(media):
    """
    Determina a situação do aluno com base na média.

    Critérios:
        média >= 7.0: Aprovado
        média >= 5.0: Recuperação
        média < 5.0: Reprovado

    Args:
        media: Média do aluno.

    Returns:
        str: Situação do aluno.

    Raises:
        ValueError: Se a média for inválida.
    """
    if not validar_nota(media):
        raise ValueError("Média inválida.")

    if media >= 7.0:
        return "Aprovado"

    if media >= 5.0:
        return "Recuperação"

    return "Reprovado"


def calcular_estatisticas(notas):
    """
    Calcula estatísticas de uma lista de notas.

    Args:
        notas: Lista de notas.

    Returns:
        dict: Dicionário com média, maior nota, menor nota,
        quantidade de aprovados, reprovados e em recuperação.

    Raises:
        ValueError: Se a lista estiver vazia ou não possuir notas válidas.
    """
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")

    notas_validas = [nota for nota in notas if validar_nota(nota)]

    if not notas_validas:
        raise ValueError("Não há notas válidas para calcular estatísticas.")

    estatisticas = {
        "media": calcular_media(notas_validas),
        "maior": max(notas_validas),
        "menor": min(notas_validas),
        "aprovados": 0,
        "reprovados": 0,
        "recuperacao": 0
    }

    for nota in notas_validas:
        situacao = obter_situacao(nota)

        if situacao == "Aprovado":
            estatisticas["aprovados"] += 1
        elif situacao == "Recuperação":
            estatisticas["recuperacao"] += 1
        else:
            estatisticas["reprovados"] += 1

    return estatisticas


def normalizar_notas(notas, nota_maxima=10):
    """
    Normaliza notas para a escala de 0 a 10.

    Args:
        notas: Lista original de notas.
        nota_maxima: Valor máximo da escala original.

    Returns:
        list: Lista de notas normalizadas.

    Raises:
        ValueError: Se nota_maxima for menor ou igual a zero.
    """
    if nota_maxima <= 0:
        raise ValueError("A nota máxima deve ser maior que zero.")

    return [(nota / nota_maxima) * 10 for nota in notas]