$(document).ready(function(){

    var pa = $('#id_char_ap');
    var pa_awk = $('#id_char_ap_despertada');
    var pd = $('#id_char_dp');
    var gs = $('#id_gs');

    pa.change(function () {
        calcula_GS();
    });
    pa_awk.change(function () {
        calcula_GS();
    });
    pd.change(function () {
        calcula_GS();
    });

    function calcula_GS () {
        if(pa.val() != '' && pa_awk.val() != '' && pd.val() != ''){
            var calcula = ((parseInt(pa.val()) + parseInt(pa_awk.val())) / 2) + parseInt(pd.val());
            gs.val(Math.ceil(calcula));
        }
    }

});