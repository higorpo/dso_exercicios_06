from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipos_chamado = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        return len([x for x in self.__chamados if x.tipo == tipo])

    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        if isinstance(data, Date) and isinstance(cliente, Cliente) and isinstance(tecnico, Tecnico) and isinstance(titulo, str) and isinstance(descricao, str) and isinstance(prioridade, int) and isinstance(tipo, TipoChamado):
            if len([x for x in self.__chamados if x.data == data and x.cliente == cliente and x.tecnico == tecnico and x.tipo == tipo]) == 0:
                chamado = Chamado(data, cliente, tecnico,
                                  titulo, descricao, prioridade, tipo)
                self.__chamados.append(chamado)
                return chamado
            else:
                return None

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        if codigo not in [tipos_chamado.codigo for tipos_chamado in self.__tipos_chamado]:
            tipoChamado = TipoChamado(codigo, descricao, nome)
            self.__tipos_chamado.append(tipoChamado)
            return tipoChamado
        else:
            return None

    @property
    def tipos_chamados(self):
        return self.__tipos_chamado
