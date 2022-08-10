# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

# # fila_teste = FilaNormal()
# # fila_teste.atualiza_fila()
# # fila_teste.atualiza_fila()
# # fila_teste.atualiza_fila()
# # print(fila_teste.chama_cliente(5))
# # print(fila_teste.chama_cliente(10))

# # fila_teste2 = FilaPrioritaria()
# # fila_teste2.atualiza_fila()
# # fila_teste2.atualiza_fila()
# # print(fila_teste2.chama_cliente(10))
# # print(fila_teste2.chama_cliente(1))
# # print(fila_teste2.estatistica("08/08/2022", 215, "detail"))

teste_fabrica = FabricaFila.pega_fila("PR")
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(5))
print(teste_fabrica.chama_cliente(3))
print(teste_fabrica.chama_cliente(2))
print(teste_fabrica.chama_cliente(4))

print(teste_fabrica.estatistica(EstatisticaResumida("20/03/2025", 120)))
print(teste_fabrica.estatistica(EstatisticaDetalhada("20/03/2025", 120)))
