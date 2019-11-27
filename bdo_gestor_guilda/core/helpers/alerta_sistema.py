from bdo_gestor_guilda.core.helpers.utils import contador_de_registros


def alerta_sistema(usuario):
    arr_texto = []
    limitador_para_alerta_por_registros = 1600
    num_registros, percent = contador_de_registros()
    contexto = {
        'exibe_alerta': False,
        'texto': arr_texto,
    }
    if int(num_registros) >= limitador_para_alerta_por_registros and usuario.is_lider():
        contexto.update({'exibe_alerta': True})
        arr_texto.append(
            '''Atualmente o seu banco de dados contem {} registros. 
            Está muito próximo do limite, faça a devida limpeza dos 
            dados em configurações.'''.format(num_registros))
        contexto.update({'texto': arr_texto})

    return contexto
