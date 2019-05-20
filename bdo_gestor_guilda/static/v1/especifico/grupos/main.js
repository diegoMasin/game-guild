$( document ).ready(function() {
    // Basic
    $('#basicTree').jstree({
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
});