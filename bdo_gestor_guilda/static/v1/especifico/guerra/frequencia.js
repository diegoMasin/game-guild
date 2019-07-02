$( document ).ready(function() {
    $('.marca-freq-player').click(function () {
        console.log($(this).val());
        console.log($(this).data('guerra-id'));
        console.log(URL_MARCAR);
        $.ajax({
            type: 'GET',
            url: URL_MARCAR,
            dataType: 'json',
            data: {
                guerra: $(this).data('guerra-id'),
                user_avancado: $(this).val(),
            },
            success: function (data) {
                console.log('Presença de ' + data.user_avancado + 'foi marcado com sucesso.');
            } 
        });
    });
});