$(document).ready(function(){
    $('.inativar-membro').click(function() {
        var titulo = $(this).data('model-title');
        var id_user_avancado = $(this).data('id-user-avancado');
        $('#titulo-modal-reprovar').text('Inativar - ' + titulo);
        $('#hidden-modal-id-user').val(id_user_avancado);
    });

    $('.inativar-heroi').click(function() {
        var titulo = $(this).data('model-title');
        var id_user_avancado = $(this).data('id-user-avancado');
        $('#titulo-modal-reprovar').text('Inativar Herói - ' + titulo);
        $('#hidden-modal-id-user').val(id_user_avancado);
    });
});
