from app.dao.dao import DAO
from app.models.usuario import Usuario


class Usuario_DAO(DAO):

    def __init__(self, database, cidade_dao, perfis_dao):
        super().__init__(database)
        self._cidade_dao = cidade_dao
        self._perfis_dao = perfis_dao

    def save(self, usuario):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    INSERT INTO USUARIO
                    (
                        NOME,
                        EMAIL,
                        DATA_NASCIMENTO,
                        CIDADE_ID,
                        PERFIS_ID
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                  """

            cursor.execute(
                sql,
                (
                    usuario.nome,
                    usuario.email,
                    usuario.data_nascimento,
                    usuario.cidade.id,
                    usuario.perfis.id
                )
            )

            conexao.commit()

            usuario.id = cursor.lastrowid

            return usuario

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
                        EMAIL,
                        DATA_NASCIMENTO,
                        CIDADE_ID,
                        PERFIS_ID
                    FROM
                        USUARIO
                    ORDER BY
                        NOME
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            usuarios = []

            for registro in registros:

                cidade = self._cidade_dao.get_by_id(
                    registro[4]
                )

                perfis = self._perfis_dao.get_by_id(registro[5])

                usuarios.append(

                    Usuario(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        cidade,
                        perfis
                    )

                )

            return usuarios

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        NOME,
                        EMAIL,
                        DATA_NASCIMENTO,
                        CIDADE_ID,
                        PERFIS_ID
                    FROM
                        USUARIO
                    WHERE
                        ID = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            cidade = self._cidade_dao.get_by_id(
                registro[4]
            )

            perfis = self._perfis_dao.get_by_id(
                registro[5]
            )

            return Usuario(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                cidade,
                perfis
            )

        finally:
            self.desconectar(cursor, conexao)

    def update(self, usuario):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    UPDATE USUARIO
                    SET
                        NOME = %s,
                        EMAIL = %s,
                        DATA_NASCIMENTO = %s,
                        CIDADE_ID = %s,
                        PERFIS_ID = %s
                    WHERE
                        ID = %s
                  """

            cursor.execute(
                sql,
                (
                    usuario.nome,
                    usuario.email,
                    usuario.data_nascimento,
                    usuario.cidade.id,
                    usuario.perfis.id,
                    usuario.id
                    
                )
            )

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def delete(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    DELETE
                    FROM USUARIO
                    WHERE
                        ID = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)