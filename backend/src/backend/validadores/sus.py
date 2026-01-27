import re

def sus_validar(sus: str) -> bool:
    # Remove caracteres não numéricos
    sus = re.sub(r'\D', '', sus)

    # CNS deve ter 15 dígitos
    if len(sus) != 15:
        return False

    # Existem três tipos de CNS válidos:
    # 1. Iniciados por 1 ou 2 (gerados a partir do CPF)
    # 2. Iniciados por 7, 8 ou 9 (gerados aleatoriamente)
    # 3. Iniciados por 3, 4, 5 ou 6 (reservados)

    # Validação para CNS iniciado por 1 ou 2
    if sus[0] in ['1', '2']:
        soma = sum(int(sus[i]) * (15 - i) for i in range(15))
        return soma % 11 == 0

    # Validação para CNS iniciado por 7, 8 ou 9
    elif sus[0] in ['7', '8', '9']:
        soma = sum(int(sus[i]) * (15 - i) for i in range(15))
        return soma % 11 == 0

    # Outros prefixos não são considerados válidos
    return False
