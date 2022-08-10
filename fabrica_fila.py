from typing import Union
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import CODIGO_NORMAL, CODIGO_PRIORITARIO


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila: str) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == CODIGO_NORMAL:
            return FilaNormal()
        elif tipo_fila == CODIGO_PRIORITARIO:
            return FilaPrioritaria()
        else:
            raise NotImplementedError("Tipo de fila nao existe!")
