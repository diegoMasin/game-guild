!function ($) {
    "use strict";

    var SweetAlert = function () {
    };

    SweetAlert.prototype.init = function () {

        //Botão de Ação Arquivar
        $('.acao-arquivar').click(function (event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');
            var titulo_botao = $(this).data('original-title');

            swal({
                title: 'Você deseja ' + titulo_botao +'?',
                text: 'Após arquivada, esta ' + titulo_model + ' sairá dos cálculos.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, ' + titulo_botao + '!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Excluída!',
                        text: 'Você ' + titulo_botao + '(ou) a ' + titulo_model + '.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });

                } else {
                    swal('Cancelada', 'Você não arquivou a ' + titulo_model + '.', 'error');
                }
            });
        });

        //Botão de Ação Excluir
        $('.acao-excluir').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Excluir?',
                text: 'Após excluída, esta ' + titulo_model + ' deixará de existir.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Excluir!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Excluída!',
                        text: 'Você Excluiu a ' + titulo_model + '.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelada', 'Você não excluiu a ' + titulo_model + '.', 'error');
                }
            });
        });

        //Botão de Ação Ativar
        $('.acao-ativar').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Recrutar/Ativar?',
                text: 'Após ativado, ' + titulo_model + ' pertencerá a Guilda OXION.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Recrutar/Ativar!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Ativado!',
                        text: 'Você Ativou ' + titulo_model + '.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelada', 'Você não ativou ' + titulo_model + '.', 'error');
                }
            });
        });

        //Botão de Ação Promover
        $('.acao-promover').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Promover?',
                text: 'Após promovido, ' + titulo_model + ' subirá à próxima patente.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Promover!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Promovido!',
                        text: 'Você Promoveu ' + titulo_model + '.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelada', 'Você não promoveu ' + titulo_model + '.', 'error');
                }
            });
        });

        //Botão de Ação Rebaixar
        $('.acao-rebaixar').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Rebaixar?',
                text: 'Após rebaixar, ' + titulo_model + ' descerá à próxima patente.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Rebaixar!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Rebaixado!',
                        text: 'Você Rebaixou ' + titulo_model + '.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelada', 'Você não rebaixou ' + titulo_model + '.', 'error');
                }
            });
        });

        //Botão de Ação Deletar Grupo Fixo
        $('.acao-deletar-grupo').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Apagar?',
                text: 'Após apagado, ' + titulo_model + ' deixará de existir.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Apagar!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Apagado!',
                        text: 'Você Apagou ' + titulo_model + '.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelado', 'Você não apagou ' + titulo_model + '.', 'error');
                }
            });
        });

    },
        //init
        $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing
    function ($) {
        "use strict";
        $.SweetAlert.init()
    }(window.jQuery);