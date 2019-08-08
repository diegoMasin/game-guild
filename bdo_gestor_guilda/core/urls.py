from django.conf.urls import url

from bdo_gestor_guilda.core.views import anuncios_gerais
from bdo_gestor_guilda.core.views import anuncios_restritos
from bdo_gestor_guilda.core.views import frequencia_guerra
from bdo_gestor_guilda.core.views import grupos
from bdo_gestor_guilda.core.views import guerras
from bdo_gestor_guilda.core.views import home
from bdo_gestor_guilda.core.views import lista_negra
from bdo_gestor_guilda.core.views import membros
from bdo_gestor_guilda.core.views import payout
from bdo_gestor_guilda.core.views import recrutas
from bdo_gestor_guilda.core.views import vinculo_grupos

urlpatterns = [
    url(r'^$', home.pagina_inicial, name='pagina_inicial'),
    url(r'^inserir-participante-guerra/$', home.inserir_participante_guerra, name='inserir_participante_guerra'),

    url(r'^recrutas/listar/$', recrutas.listar, name='recrutas_listar'),
    url(r'^recrutas/recrutar_ativar/(?P<user_avancado_id>(\d+))/$', recrutas.recrutar_ativar,
        name='recrutas_recrutar_ativar'),
    url(r'^recrutas/recrutar_ativar_heroi/(?P<user_avancado_id>(\d+))/$', recrutas.recrutar_ativar_heroi,
        name='recrutas_recrutar_ativar_heroi'),
    url(r'^recrutas/recrutar_reprovar/$', recrutas.recrutar_reprovar, name='recrutar_reprovar'),

    url(r'^membros/listar/$', membros.listar, name='membros_listar'),
    url(r'^membros/promover/(?P<user_avancado_id>(\d+))/$', membros.promover, name='membros_promover'),
    url(r'^membros/rebaixar/(?P<user_avancado_id>(\d+))/$', membros.rebaixar, name='membros_rebaixar'),
    url(r'^membros/inativar/$', membros.inativar, name='membros_inativar'),
    url(r'^membros/tornar-heroi/(?P<user_avancado_id>(\d+))/$', membros.tornar_heroi, name='membros_tornar_heroi'),
    url(r'^herois/listar/$', membros.listar_herois, name='herois_listar'),
    url(r'^herois/tornar-membro/(?P<user_avancado_id>(\d+))/$', membros.tornar_membro, name='herois_tornar_membro'),

    url(r'^grupos/listar/$', grupos.listar, name='grupos_listar'),
    url(r'^grupos/cadastrar/$', grupos.cadastrar, name='grupos_cadastrar'),
    url(r'^grupos/inserir/$', grupos.inserir, name='grupos_inserir'),
    url(r'^grupos/editar/(?P<grupo_id>(\d+))/$', grupos.editar, name='grupos_editar'),
    url(r'^grupos/atualizar/(?P<grupo_id>(\d+))/$', grupos.atualizar, name='grupos_atualizar'),
    url(r'^grupos/deletar/(?P<grupo_id>(\d+))/$', grupos.deletar, name='grupos_deletar'),

    url(r'^vinculo-grupos/cadastrar/$', vinculo_grupos.cadastrar, name='vinculo_grupos_cadastrar'),
    url(r'^vinculo-grupos/inserir/$', vinculo_grupos.inserir, name='vinculo_grupos_inserir'),
    url(r'^vinculo-grupos/deletar/(?P<vinculo_grupo_id>(\d+))/$', vinculo_grupos.deletar, name='vinculo_grupos_deletar'),

    url(r'^anuncios-gerais/cadastrar/$', anuncios_gerais.cadastrar, name='anuncios_gerais_cadastrar'),
    url(r'^anuncios-gerais/inserir/$', anuncios_gerais.inserir, name='anuncios_gerais_inserir'),
    url(r'^anuncios-gerais/deletar/$', anuncios_gerais.deletar, name='anuncios_gerais_deletar'),
    url(r'^anuncios-restritos/cadastrar/$', anuncios_restritos.cadastrar, name='anuncios_restritos_cadastrar'),
    url(r'^anuncios-restritos/inserir/$', anuncios_restritos.inserir, name='anuncios_restritos_inserir'),
    url(r'^anuncios-restritos/deletar/$', anuncios_restritos.deletar, name='anuncios_restritos_deletar'),

    url(r'^guerras/listar/$', guerras.listar, name='guerras_listar'),
    url(r'^guerras/cadastrar/$', guerras.cadastrar, name='guerras_cadastrar'),
    url(r'^guerras/inserir/$', guerras.inserir, name='guerras_inserir'),
    url(r'^guerras/editar/(?P<guerra_id>(\d+))/$', guerras.editar, name='guerras_editar'),
    url(r'^guerras/atualizar/(?P<guerra_id>(\d+))/$', guerras.atualizar, name='guerras_atualizar'),
    url(r'^guerras/excluir/(?P<guerra_id>(\d+))/$', guerras.excluir, name='guerras_excluir'),

    url(r'^lista-negra/listar/$', lista_negra.listar, name='lista_negra_listar'),
    url(r'^lista-negra/reativar/(?P<user_avancado_id>(\d+))/$', lista_negra.reativar, name='lista_negra_reativar'),
    url(r'^lista-negra/reativar-heroi/(?P<user_avancado_id>(\d+))/$', lista_negra.reativar_heroi,
        name='lista_negra_reativar_heroi'),

    url(r'^frequencia-guerra/listar/(?P<guerra_id>(\d+))/$', frequencia_guerra.listar, name='frequencia_guerra_listar'),
    url(r'^frequencia-guerra/marcar/$', frequencia_guerra.marcar, name='frequencia_guerra_marcar'),

    url(r'^payout/listar/$', payout.listar, name='payout_listar'),
    url(r'^payout/cadastrar/$', payout.cadastrar, name='payout_cadastrar'),
    url(r'^payout/inserir/$', payout.inserir, name='payout_inserir'),
    url(r'^payout/editar/(?P<payout_id>(\d+))/$', payout.editar, name='payout_editar'),
    url(r'^payout/atualizar/(?P<payout_id>(\d+))/$', payout.atualizar, name='payout_atualizar'),
    url(r'^payout/excluir/(?P<payout_id>(\d+))/$', payout.excluir, name='payout_excluir'),
    url(r'^payout/listar_calculos/(?P<payout_id>(\d+))/$', payout.listar_calculos, name='payout_listar_calculos'),
    url(r'^payout/adicionar-tier/$', payout.adicionar_tier, name='payout_adicionar_tier'),

]
