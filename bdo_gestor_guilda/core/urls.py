from django.conf.urls import url
from bdo_gestor_guilda.core.views import home
from bdo_gestor_guilda.core.views import recrutas
from bdo_gestor_guilda.core.views import membros
from bdo_gestor_guilda.core.views import grupos
from bdo_gestor_guilda.core.views import vinculo_grupos

urlpatterns = [
    url(r'^$', home.pagina_inicial, name='pagina_inicial'),

    url(r'^recrutas/listar/$', recrutas.listar, name='recrutas_listar'),
    url(r'^recrutas/recrutar_ativar/(?P<user_avancado_id>(\d+))/$', recrutas.recrutar_ativar,
        name='recrutas_recrutar_ativar'),
    url(r'^recrutas/recrutar_reprovar/$', recrutas.recrutar_reprovar, name='recrutar_reprovar'),

    url(r'^membros/listar/$', membros.listar, name='membros_listar'),
    url(r'^membros/promover/(?P<user_avancado_id>(\d+))/$', membros.promover, name='membros_promover'),
    url(r'^membros/rebaixar/(?P<user_avancado_id>(\d+))/$', membros.rebaixar, name='membros_rebaixar'),

    url(r'^grupos/listar/$', grupos.listar, name='grupos_listar'),
    url(r'^grupos/cadastrar/$', grupos.cadastrar, name='grupos_cadastrar'),
    url(r'^grupos/inserir/$', grupos.inserir, name='grupos_inserir'),
    url(r'^grupos/deletar/(?P<grupo_id>(\d+))/$', grupos.deletar, name='grupos_deletar'),

    url(r'^vinculo-grupos/cadastrar/$', vinculo_grupos.cadastrar, name='vinculo_grupos_cadastrar'),
    url(r'^vinculo-grupos/inserir/$', vinculo_grupos.inserir, name='vinculo_grupos_inserir'),

    # PADRÃO DE URLS DO SISTEMA SIC
    # url(r'^contas/$', contas.listar, name='contas_listar'),
    # url(r'^contas/salvar$', contas.salvar, name='contas_salvar'),
    # url(r'^contas/arquivar/(?P<id_conta>(\d+))/$', contas.arquivar, name='contas_arquivar'),
    # url(r'^contas/editar/$', contas.editar, name='contas_editar'),
    # url(r'^contas/atualizar/$', contas.atualizar, name='contas_atualizar'),
    #
    #
    # url(r'^tags/$', tags.listar, name='tags_listar'),
    # url(r'^tags/salvar/$', tags.salvar, name='tags_salvar'),
    # url(r'^tags/apagar/(?P<id_tag>(\d+))/$', tags.apagar, name='tags_apagar'),
    # url(r'^tags/editar/$', tags.editar, name='tags_editar'),
    # url(r'^tags/atualizar/$', tags.atualizar, name='tags_atualizar'),
    #
    # url(r'^tipo_despesa/$', tipo_despesa.listar, name='tipo_despesa_listar'),
    # url(r'^tipo_despesa/salvar/$', tipo_despesa.salvar, name='tipo_despesa_salvar'),
    # url(r'^tipo_despesa/apagar/(?P<id_tipo_despesa>(\d+))/$', tipo_despesa.apagar, name='tipo_despesa_apagar'),
    # url(r'^tipo_despesa/editar/$', tipo_despesa.editar, name='tipo_despesa_editar'),
    # url(r'^tipo_despesa/atualizar/$', tipo_despesa.atualizar, name='tipo_despesa_atualizar'),
    #
    # url(r'^tipo_receita/$', tipo_receita.listar, name='tipo_receita_listar'),
    # url(r'^tipo_receita/salvar/$', tipo_receita.salvar, name='tipo_receita_salvar'),
    # url(r'^tipo_receita/apagar/(?P<id_tipo_receita>(\d+))/$', tipo_receita.apagar, name='tipo_receita_apagar'),
    # url(r'^tipo_receita/editar/$', tipo_receita.editar, name='tipo_receita_editar'),
    # url(r'^tipo_receita/atualizar/$', tipo_receita.atualizar, name='tipo_receita_atualizar'),
]
