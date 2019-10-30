!function($) {
    "use strict";

    var MorrisCharts = function () {
    };

    //Participação e Frequência em NodeWar / Siege por Dia
    MorrisCharts.prototype.createLineChart = function(element, data, xkey, ykeys, labels, opacity, Pfillcolor, Pstockcolor, lineColors) {
        Morris.Line({
            element: element,
            data: data,
            xkey: xkey,
            ykeys: ykeys,
            labels: labels,
            fillOpacity: opacity,
            pointFillColors: Pfillcolor,
            pointStrokeColors: Pstockcolor,
            behaveLikeLine: true,
            gridLineColor: '#999',
            hideHover: 'auto',
            resize: true, //defaulted to true
            lineColors: lineColors,
            parseTime: false,
            gridIntegers: true,
            ymin: 0
        });
    },

    MorrisCharts.prototype.init = function() {
        var dicionario = JSON_GRAFICO_GUERRA_DIA;
        var $data = [];
        function montaGraficoGuerraDia(value, index, array) {
            var participacoes = value.participacoes;
            var frequencias = value.frequencias;
            var dias = value.dia;
            if(participacoes == null) {
                participacoes = 0
            }
            if(frequencias == null) {
                frequencias = 0
            }
            $data.push({y: dias, a: participacoes, b: frequencias})
        }
        dicionario.forEach(montaGraficoGuerraDia);
        this.createLineChart('morris-line-example', $data, 'y', ['a', 'b'], ['Participações', 'Frequências'],
            ['0.1'],['#fff'],['#000'], ['#163282', '#14aa41']);
    },
    //init
    $.MorrisCharts = new MorrisCharts, $.MorrisCharts.Constructor = MorrisCharts

}(window.jQuery),

//initializing
    function($) {
        "use strict";
        $.MorrisCharts.init();
    }(window.jQuery);
