from django.conf.urls import url

from bdo_gestor_guilda.usuario import views as usuario_view

urlpatterns = [
    url(r'^login/$', usuario_view.do_login, name='usuario_login'),
    url(r'^logout/$', usuario_view.do_logout, name='usuario_logout'),
    url(r'^signup/$', usuario_view.signup, name='usuario_signup'),
    url(r'^cadastrar-user-avancado/$', usuario_view.cadastrar_user_avancado, name='cadastrar_user_avancado'),
    url(r'^inserir-user-avancado/$', usuario_view.inserir_user_avancado, name='inserir_user_avancado'),
    url(r'^aguarde-aprovacao/$', usuario_view.aguarde_aprovacao, name='usuario_aguarde_aprovacao'),
    url(r'^editar-perfil/$', usuario_view.editar_perfil, name='usuario_editar_perfil'),
    url(r'^atualizar-perfil/(?P<user_avancado_id>(\d+))/$', usuario_view.atualizar_perfil,
        name='usuario_atualizar_perfil'),
]
