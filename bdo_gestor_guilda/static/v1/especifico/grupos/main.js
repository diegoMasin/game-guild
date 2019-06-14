$( document ).ready(function() {
    // Basic
    $('.arvore-grupo').jstree({
        'core' : {
            'themes' : {
                'responsive': false
            }
        },
        'types' : {
            'default' : {
                'icon' : 'fa-2x mdi mdi-account-star'
            },
            'file' : {
                'icon' : 'fa fa-file'
            }
        },
        'plugins' : ['types']
    });

    // Interações específicas
    $('#exp_grupos').click(function () {
        $('li.jstree-closed > i.jstree-ocl').trigger('click');
        $('#exp_grupos').hide();
        $('#col_grupos').show();
    });

    $('#col_grupos').click(function () {
        $('li.jstree-open > i.jstree-ocl').trigger('click');
        $('#col_grupos').hide();
        $('#exp_grupos').show();
    });
});