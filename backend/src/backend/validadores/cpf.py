import re

def cpf_validar(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)

    # CPF deve ter 11 dígitos
    if len(cpf) != 11:
        return False

    # Elimina CPFs com todos os dígitos iguais (ex.: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return False

    # Calcula primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    digito1 = 0 if digito1 == 10 else digito1

    # Calcula segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    digito2 = 0 if digito2 == 10 else digito2

    # Verifica se os dígitos calculados batem com os informados
    return cpf[-2:] == f"{digito1}{digito2}"

