class Perfil_Fornecedor_Controller:

    def __init__(
        self,
        dao,
        fornecedor_dao,
        view
    ):
        self.dao = dao
        self.fornecedor_dao = fornecedor_dao
        self.view = view

    def abrir_fornecedores(self, perfil):

        try:

            fornecedores = self.fornecedor_dao.get_all()

            perfil.fornecedores = self.dao.get_fornecedores_por_perfil(
                perfil
            )

            return fornecedores

        except Exception as e:

            if self.view is not None:
                self.view.exibir_mensagem(
                    f"Erro ao carregar fornecedores: {str(e)}",
                    False
                )

            return []

    def salvar_fornecedores(
        self,
        view,
        perfil,
        fornecedores
    ):

        try:

            self.dao.substituir_fornecedores_do_perfil(
                perfil,
                fornecedores
            )

            perfil.fornecedores = fornecedores

            view.exibir_mensagem(
                "Fornecedores do perfil atualizados com sucesso!"
            )

            view.fechar()

        except Exception as e:

            view.exibir_mensagem(
                f"Erro ao salvar fornecedores: {str(e)}",
                False
            )