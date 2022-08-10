# def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
#     estatistica: Dict[str, Union[List[str], str, int]] = {}
#     if flag != "detail":
#         estatistica[f"{agencia}-{dia}"] = len(self.clientes_atendidos)
#     else:
#         estatistica["Dia"] = dia
#         estatistica["Agencia"] = agencia
#         estatistica["Clientes Atendidos"] = self.clientes_atendidos
#         estatistica["Quantidade Clientes Atendidos"] = len(
#             self.clientes_atendidos
#         )
#     return estatistica
