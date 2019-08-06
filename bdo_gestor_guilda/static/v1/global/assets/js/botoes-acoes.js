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

        //Botão de Ação Deletar Grupo Fixo
        $('.acao-remover-vinculo-grupo').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Remover?',
                text: 'Após removido, ' + titulo_model + ' sairá do grupo.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Remover!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Removido!',
                        text: 'Você Removeu ' + titulo_model + '.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelado', 'Você não removeu ' + titulo_model + '.', 'error');
                }
            });
        });

        //Botão de Ação Limpar Anúncios
        $('.acao-limpar-anuncio').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Limpar o Anúncio abaixo?',
                text: 'Após excluído, o anúncio deixará de existir.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Limpar!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Removido!',
                        text: 'Você Limpou o Anúncio abaixo.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelado', 'Você não limpou o anúncio.', 'error');
                }
            });
        });

        //Botão de Ação Reativar Ex-membro
        $('.acao-reativar-membro').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Reativar ' + titulo_model + ' ?',
                text: 'Após reativado, ' + titulo_model + ' voltará a ser Membro da Guilda.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Reativar!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Reativado!',
                        text: 'Você Reativou ' + titulo_model + '.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelado', 'Você não reativou ' + titulo_model + '.', 'error');
                }
            });
        });

        //Botão de Ação Reativar Ex-heroi
        $('.acao-reativar-heroi').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Reativar ' + titulo_model + ' como Herói?',
                text: 'Após reativado, ' + titulo_model + ' voltará a ser Herói da Guilda.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Reativar Herói!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Herói Reativado!',
                        text: 'Você Reativou ' + titulo_model + ' como Herói.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelado', 'Você não reativou ' + titulo_model + '.', 'error');
                }
            });
        });

        //Botão de Ação Tornar Heroi
        $('.acao-tornar-heroi').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Tornar ' + titulo_model + ' um Herói?',
                text: 'Após esta ação, ' + titulo_model + ' será um Herói da Guilda.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Tornar Herói!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Agora é um Herói!',
                        text: 'Você tornou ' + titulo_model + ' um Herói.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelado', 'Você não tornou ' + titulo_model + ' um Herói.', 'error');
                }
            });
        });

        //Botão de Ação Tornar Membro
        $('.acao-tornar-membro').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: 'Você deseja Tornar ' + titulo_model + ' um Membro?',
                text: 'Após esta ação, ' + titulo_model + ' será um Membro da Guilda.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#DD6B55',
                confirmButtonText: 'Sim, Tornar Membro!',
                cancelButtonText: 'Não, Cancele!',
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Agora é um Membro!',
                        text: 'Você tornou ' + titulo_model + ' um Membro.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal('Cancelado', 'Você não tornou ' + titulo_model + ' um Membro.', 'error');
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