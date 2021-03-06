(function($) {

    // GERADO DE MENSAGENS
    if($('.gerado-mensagem').length) {
        $('.gerado-mensagem').click();
    }

    // GERADOR DA MASCARA MOEDA REAL
    if($('.moeda-real').length) {
        $('.moeda-real').maskMoney({
            prefix:'R$ ',
            allowNegative: true,
            thousands:'.',
            decimal:',',
            affixesStay: true
        });
    }

    // RETIRA FORMATAÇÃO MOEDA
    function remove_format_moeda(value) {
        value = value.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.');
        value = parseFloat(value);

        return value;
    }

    // SELECT2
    $('.select2').select2();

    // DATE PICKER
    $('.date-picker-default').datepicker({
        autoclose: true,
        todayHighlight: true,
        format: 'dd/mm/yyyy'
    });
})
(jQuery);
