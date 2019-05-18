$(document).ready(function(){
    $('.reprovar-recruta').click(function() {
        var titulo = $(this).data('model-title');
        var id_user_avancado = $(this).data('id-user-avancado');
        $('#titulo-modal-reprovar').text('Reprovar Recruta - ' + titulo);
        $('#hidden-modeal-id-user').val(id_user_avancado);
    });
})
