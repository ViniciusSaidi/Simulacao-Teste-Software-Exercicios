def _apenas_digitos(cpf: str) -> str:
    if cpf is None:
        return ""

    return "".join(char for char in cpf if char.isdigit())


def validar_cpf(cpf: str) -> bool:
    cpf = _apenas_digitos(cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = soma % 11
    primeiro_digito = 0 if resto < 2 else 11 - resto

    if int(cpf[9]) != primeiro_digito:
        return False

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = soma % 11
    segundo_digito = 0 if resto < 2 else 11 - resto

    return int(cpf[10]) == segundo_digito


def formatar_cpf(cpf: str) -> str:
    cpf_limpo = _apenas_digitos(cpf)

    if not validar_cpf(cpf_limpo):
        raise ValueError("CPF inválido")

    return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"