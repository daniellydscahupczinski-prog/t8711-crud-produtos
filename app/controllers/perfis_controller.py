from app.models.perfis import Perfis
from app.core.idioma import Idioma

class Perfis_controller:

    def __init__(
        self,
        dao,
        perfis_dao,
        perfil_fornecedor_controller,
        view
    ):
        self.dao = dao
        self.perfis_dao = perfis_dao
        self.perfil_fornecedor_controller = perfil_fornecedor_controller
        self.view = view
        self.perfis_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def carregar_perfis(self):
        perfis = self.perfis_dao.get_all()
        self.view.exibir_perfis(perfis)

    def save(self):
        try:
            nome, descricao = self.view.ler_dados_perfil()

            perfis = Perfis(
                None,
                nome,
                descricao
            )

            self.dao.save(perfis)
            self.carregar_perfis()

            self.view.exibir_mensagem(
                (Idioma.t("perfis.cadastrado"))
            )

        except ValueError:
            self.view.exibir_mensagem(
                (Idioma.t("perfis.erro")),
                False
            )

    def selecionar_perfis(self, event):
        try:
            id_perfis = self.view.get_id_selecionado()

            self.perfis_selecionado = self.dao.get_by_id(
                id_perfis
            )

            self.view.preencher_campos(
                self.perfis_selecionado
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.perfis_selecionado is None:
                self.view.exibir_mensagem(
                    (Idioma.t("perfis.selecionar_lista")),
                    False
                )
                return

            nome, descricao = self.view.ler_dados_perfil()

            self.perfis_selecionado.atualizar_dados(
                nome,
                descricao
            )

            self.dao.update(
                self.perfis_selecionado
            )

            self.carregar_perfis()

            self.view.exibir_mensagem(
                (Idioma.t("perfis.atualizado"))
            )

        except ValueError as e:
            self.view.exibir_mensagem(
                f"Erro: {str(e)}",
                False
            )

    def delete(self):
        if self.perfis_selecionado is None:
            self.view.exibir_mensagem(
                (Idioma.t("perfis.selecionar_lista")),
                False
            )
            return

        if not self.view.confirmar_exclusão():
            return

        try:
            sucesso = self.dao.delete(
                self.perfis_selecionado.id
            )

            if sucesso:
                self.perfis_selecionado = None

                self.view.limpar_campos()
                self.carregar_perfis()

                self.view.exibir_mensagem(
                    (Idioma.t("perfis.excluido"))
                )

            else:
                self.view.exibir_mensagem(
                    (Idioma.t("perfis.nao_encontrado")),
                    False
                )

        except Exception as e:
            self.view.exibir_mensagem(
                (Idioma.t("perfis.problemas_excluir")),
                False
            )