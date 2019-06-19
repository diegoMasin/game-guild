from django.conf.urls import url

from bdo_gestor_guilda.usuario import views as usuario_view

urlpatterns = [
    url(r'^login/$', usuario_view.do_login, name='usuario_login'),
    url(r'^logout/$', usuario_view.do_logout, name='usuario_logout'),
    url(r'^signup/$', usuario_view.signup, name='usuario_signup'),
    url(r'^termo-de-uso/$', usuario_view.termo, name='usuario_termo'),
    url(r'^cadastrar-user-avancado/$', usuario_view.cadastrar_user_avancado, name='cadastrar_user_avancado'),
    url(r'^inserir-user-avancado/$', usuario_view.inserir_user_avancado, name='inserir_user_avancado'),
    url(r'^aguarde-aprovacao/$', usuario_view.aguarde_aprovacao, name='usuario_aguarde_aprovacao'),
    url(r'^editar-perfil/$', usuario_view.editar_perfil, name='usuario_editar_perfil'),
    url(r'^atualizar-perfil/(?P<user_avancado_id>(\d+))/$', usuario_view.atualizar_perfil,
        name='usuario_atualizar_perfil'),

    url(r'^reset-senha/$', usuario_view.reset_senha, name='reset_senha'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
