def detectar_substantivo_solicitacao(substantivos_solicitacao:list, linha_normalizada: str) -> str | None:
    for s in substantivos_solicitacao:
        if s in linha_normalizada:
            return s
    return None