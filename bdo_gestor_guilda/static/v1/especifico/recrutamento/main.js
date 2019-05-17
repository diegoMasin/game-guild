$(document).ready(function(){
    $('.reprovar-recruta').click(function() {
        var titulo = $(this).data('model-title');
        $('#titulo-modal-reprovar').text('Reprovar Recruta - ' + titulo);
    });
})
