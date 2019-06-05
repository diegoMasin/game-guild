from django.conf.urls import url
from bdo_gestor_guilda.core.views import home
from bdo_gestor_guilda.core.views import recrutas
from bdo_gestor_guilda.core.views import membros
from bdo_gestor_guilda.core.views import grupos
from bdo_gestor_guilda.core.views import vinculo_grupos
from bdo_gestor_guilda.core.views import anuncios_gerais
from bdo_gestor_guilda.core.views import anuncios_restritos
from bdo_gestor_guilda.core.views import guerras

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

]
