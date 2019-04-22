$(window).on('load', function() {
    $('.foo-table-default').footable();

    var filtrando = $('.foo-table-default');
    filtrando.footable().on('footable_filtering', function(e) {});

    $('.input-foo-search').on('input', function(e) {
        e.preventDefault();
        filtrando.trigger('footable_filter', {filter: $(this).val()});
    });

});
