from app.dao.dao import DAO
from app.models.perfis import Perfis

class Perfis_DAO(DAO):
    def __init__(self, database, usuario_dao):
        super().__init__(database)
        self._usuario_dao = usuario_dao

    def save(self,perfis):
        conexao, cursor = self.conectar()
        try:
            sql = """
                        INSERT INTO PERFIS
                        (NOME, DESCRICAO)
                        VALUES (%s, %s)
                        """
            cursor.execute(sql,(
                perfis.nome,
                perfis.descricao
            ))
            conexao.commit()
            perfis.id = cursor.lastrowid
            return perfis
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)

    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                        SELECT
                            ID,
                            NOME,
                            DESCRICAO,
                            USUARIO_ID
                        FROM
                            PERFIS
                        ORDER BY
                            NOME
                            """
            cursor.execute(sql)
            registros = cursor.fetchall()
            perfis = []
            for registro in registros:
                usuario = self._usuario_dao.get_by_id(registro[3])
                perfis.append(
                    Perfis(
                        registro[0],
                        registro[1],
                        registro[2],
                        usuario
                    )
                )
            return perfis
        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =  """
                        SELECT
                            ID,
                            NOME,
                            DESCRICAO,
                            USUARIO_ID
                        FROM
                            PERFIS
                        WHERE 
                            ID = %s
                        """
            cursor.execute(sql,(id,))
            registro = cursor.fetchone()

            if registro is None:
                return None

            usuario = self._usuario_dao.get_by_id(registro[3])

            return Perfis(
                registro[0],
                registro[1],
                registro[2],
                usuario
            )
        finally:
            self.desconectar(cursor, conexao)

    def update(self, perfis):
        conexao, cursor = self.conectar()
        try:
            sql = """
                        UPDATE PRODUTO SET
                            NOME = %s,
                            DESCRICAO = %s,
                            USUARIO_ID = %s
                        WHERE
                            ID = %s
                            """
            cursor.execute(sql, (
                                        perfis.nome,
                                        perfis.descricao,
                                        perfis.usuario.id,
                                        perfis.id
            ))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)


    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                        DELETE FROM PERFIS
                        WHERE ID = %s
                        """
            cursor.execute(sql, (id,))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor,conexao)