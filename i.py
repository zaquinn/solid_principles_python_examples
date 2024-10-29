from abc import ABC, abstractmethod

# SEM ISP


class Aves(ABC):
    @abstractmethod
    def voar(self) -> str: ...

    @abstractmethod
    def bicar(self) -> str: ...


class Papagaio(Aves):
    def voar(self) -> str:
        return "voando..."

    def bicar(self) -> str:
        return "bicando..."


class Pinguim(Aves):
    def voar(self): ...

    def bicar(self) -> str:
        return "bicando..."


# COM ISP


class AvesISP(ABC):
    @abstractmethod
    def bicar(self) -> str: ...


class AvesQueVoam(AvesISP):
    @abstractmethod
    def voar(self) -> str: ...


class PapagaioISP(AvesQueVoam):
    def voar(self) -> str:
        return "voando..."

    def bicar(self) -> str:
        return "bicando..."


class PinguimISP(AvesISP):
    def bicar(self) -> str:
        return "bicando..."


if __name__ == "__main__":
    p1 = Pinguim()
    print(p1.voar())
    p2 = PinguimISP()
    print(p2.bicar())
