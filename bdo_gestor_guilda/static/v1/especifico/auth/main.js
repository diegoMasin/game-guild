/** SIGNUP **/
function showMessageNotify() {
    var mensagem = $('#senha-diverge');
    mensagem.click();
}

function validPasswordsEqual(inputs) {
    if ($(inputs[1]).val() !== $(inputs[0]).val() || (!$.trim($(inputs[1]).val()) && !$.trim($(inputs[0]).val()))) {
        showMessageNotify();
        $(inputs).parents('.input-group').addClass('has-warning');
        $(inputs).val('');
        $(inputs[0]).focus();
        return false;
    } else {
        if ($(inputs).parents('.input-group').hasClass('has-warning')) {
            $(inputs).parents('.input-group').removeClass('has-warning');
        }
        return true;
    }
}

$(document).ready(function(){

    var inputs = $('form').find('input[type="password"]');

    if (inputs !== 'undefined') {
        $(inputs[1]).focusout(function () {
            validPasswordsEqual(inputs);
        });

        $('form').submit(function(e) {
            if (!validPasswordsEqual(inputs)) {
                e.preventDefault();
                return false;
            }
        });
    }

    $('#concorda-termo').click(function () {
        $('#checkbox-signup').attr('checked', true);
    });

});
