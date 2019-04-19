from django.conf.urls import url

from bdo_gestor_guilda.usuario import views as usuario_view

urlpatterns = [
    url(r'^login/$', usuario_view.do_login, name='usuario_login'),
    url(r'^logout/$', usuario_view.do_logout, name='usuario_logout'),
    url(r'^signup/$', usuario_view.signup, name='usuario_signup'),
    url(r'^Termo_de_Uso/$', usuario_view.termo, name='usuario_termo'),
]
