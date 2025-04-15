import conexao

def ProximoId(contadorId):
    contadorRef = conexao.db.reference(contadorId)
    def incrementarId(valorAtual):
        if valorAtual is None:
            return 1
        else:
            return valorAtual + 1
    return contadorRef.transaction(incrementarId)