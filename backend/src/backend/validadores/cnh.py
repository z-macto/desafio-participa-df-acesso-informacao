import re

def cnh_validar(cnh: str) -> bool:
    # Remove caracteres não numéricos
    cnh = re.sub(r'\D', '', cnh)

    # CNH deve ter 11 dígitos
    if len(cnh) != 11:
        return False

    # Elimina CNHs com todos os dígitos iguais (ex.: 11111111111)
    if cnh == cnh[0] * 11:
        return False

    # Calcula primeiro dígito verificador
    soma = sum(int(cnh[i]) * (9 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto >= 10 else resto

    # Calcula segundo dígito verificador
    soma = sum(int(cnh[i]) * (i + 1) for i in range(9)) + digito1 * 9
    resto = soma % 11
    digito2 = 0 if resto >= 10 else resto

    # Verifica se os dígitos calculados batem com os informados
    return cnh[-2:] == f"{digito1}{digito2}"
