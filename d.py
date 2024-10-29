from abc import ABC, abstractmethod

# SEM DIP


class ConectorMySQL:
    def conectar(self) -> str:
        return "conectado no MySQL sem DIP"


class Usuarios:
    __banco_de_dados = ConectorMySQL()

    def conexao(self) -> str:
        return self.__banco_de_dados.conectar()

    def exibir_usuarios(self) -> list[str]:
        print(self.conexao())
        return print("usuários registrados sem DIP", ["João, Maria, Jorge"])


# COM DIP


class IConexaoComBanco(ABC):
    @abstractmethod
    def conectar(self) -> str: ...


class IRepositorioUsuarios(ABC):
    @abstractmethod
    def listar_usuarios(self) -> list[str]: ...


class DIPConectorMySQL(IConexaoComBanco):
    def conectar(self) -> str:
        return "conectado no MySQL com DIP..."


class DIPConectorPostgreSQL(IConexaoComBanco):
    def conectar(self) -> str:
        return "conectado no PostgreSQL com DIP..."


class RepositorioUsuariosDIP(IRepositorioUsuarios):
    def __init__(self, banco_de_dados: IConexaoComBanco):
        self.__banco_de_dados = banco_de_dados

    def listar_usuarios(self) -> list[str]:
        print(self.__banco_de_dados.conectar())
        return ["João, Maria, Jorge"]


class UsuariosDIP:
    # injeçao de dependencia
    def __init__(self, repositorio_usuarios: IRepositorioUsuarios):
        self.__repositorio_usuarios = repositorio_usuarios

    def exibir_usuarios(self):
        print(
            "usuários registrados com DIP: ",
            self.__repositorio_usuarios.listar_usuarios(),
        )


if __name__ == "__main__":
    u1 = Usuarios()
    u1.exibir_usuarios()
    print("=" * 30)
    mysql_database = DIPConectorMySQL()
    postgreqsl_database = DIPConectorPostgreSQL()
    mysql_repositorio = RepositorioUsuariosDIP(mysql_database)
    postgresql_repositorio = RepositorioUsuariosDIP(postgreqsl_database)

    u2 = UsuariosDIP(mysql_repositorio)
    u2.exibir_usuarios()
    print("=" * 30)
    u3 = UsuariosDIP(postgresql_repositorio)
    u3.exibir_usuarios()
