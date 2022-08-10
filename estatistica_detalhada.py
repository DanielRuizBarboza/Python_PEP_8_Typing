from typing import List, Dict, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {
            "Dia": self.dia, "Agencia": self.agencia,
            "Clientes Atendidos": clientes_atendidos,
            "Quantidade Clientes Atendidos": len(
                clientes_atendidos
            )}
        return estatistica
