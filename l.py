from collections.abc import Mapping

# SEM LSP


class A:
    def get_nome(self) -> str:
        return "Oi, eu sou A"


class B(A):
    def get_nome(self) -> Mapping[str, str]:
        return {"message": "Oi eu sou B"}


# COM LSP


class ALSP:
    def get_nome(self) -> str:
        return "Oi, eu sou A"


class BLSP(ALSP):
    def get_nome(self) -> str:
        return "Oi, eu sou B"


if __name__ == "__main__":
    o1: B = A()
    o2: BLSP = ALSP()
    print(o1.get_nome())
    print(o2.get_nome())
