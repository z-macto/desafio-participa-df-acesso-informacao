def _detectar_substantivo_solicitacao(self, linha_normalizada: str) -> str | None:
    for s in self.substantivos_solicitacao:
        if s in linha_normalizada:
            return s
    return None