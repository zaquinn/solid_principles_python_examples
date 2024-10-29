from abc import ABC, abstractmethod

# SEM OCP


class ContratoClt:
    def salario(self) -> int:
        return 2000


class Estagio:
    def bolsa_auxilio(self) -> int:
        return 1200


class FolhaDePagamento:
    _saldo: int

    def calcular(self, funcionario) -> int:
        if isinstance(funcionario, ContratoClt):
            self._saldo = funcionario.salario()
        elif isinstance(funcionario, Estagio):
            self._saldo = funcionario.bolsa_auxilio()
        return self._saldo


# COM OCP


class IRemuneravel(ABC):
    @abstractmethod
    def remuneracao(self) -> int: ...


class ContratoCltOCP(IRemuneravel):
    def remuneracao(self) -> int:
        return 2000


class EstagioOCP(IRemuneravel):
    def remuneracao(self) -> int:
        return 1200


class FolhaDePagamentoOCP:
    _saldo: int

    def calcular(self, funcionario: IRemuneravel) -> int:
        self._saldo = funcionario.remuneracao()
        return self._saldo


if __name__ == "__main__":
    p1 = FolhaDePagamento().calcular(ContratoClt())
    print(p1)
    p2 = FolhaDePagamentoOCP().calcular(ContratoCltOCP())
    print(p2)
