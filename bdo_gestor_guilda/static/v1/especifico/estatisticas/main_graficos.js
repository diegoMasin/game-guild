!(function($) {
  "use strict";

  var MorrisCharts = function() {};

  //Participação e Frequência em NodeWar / Siege por Dia
  (MorrisCharts.prototype.createLineChart = function(
    element,
    data,
    xkey,
    ykeys,
    labels,
    opacity,
    Pfillcolor,
    Pstockcolor,
    lineColors
  ) {
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
      gridLineColor: "#eee",
      hideHover: "auto",
      resize: true, //defaulted to true
      lineColors: lineColors,
      parseTime: false,
      gridIntegers: true,
      ymin: 0,
      yLabelFormat: y => {
        return y != Math.round(y) ? "" : y;
      }
      // xLabelAngle: -60
    });
  }),
    //Quantidade de Membros e Heróis em Siege
    (MorrisCharts.prototype.createStackedChart = function(
      element,
      data,
      xkey,
      ykeys,
      labels,
      lineColors
    ) {
      Morris.Bar({
        element: element,
        data: data,
        xkey: xkey,
        ykeys: ykeys,
        stacked: true,
        labels: labels,
        hideHover: "auto",
        resize: true, //defaulted to true
        gridLineColor: "#eeeeee",
        barColors: lineColors
      });
    }),
    (MorrisCharts.prototype.createDonutChart = function(element, data, colors) {
      Morris.Donut({
        element: element,
        data: data,
        resize: true, //defaulted to true
        colors: colors
      });
    }),
    (MorrisCharts.prototype.init = function() {
      var dicionario_guerra_dia = JSON_GRAFICO_GUERRA_DIA;
      var $data = [];
      function montaGraficoGuerraDia(value, index, array) {
        var participacoes = value.participacoes;
        var frequencias = value.frequencias;
        var dias = value.dia;
        if (participacoes == null) {
          participacoes = 0;
        }
        if (frequencias == null) {
          frequencias = 0;
        }
        $data.push({ y: dias, a: participacoes, b: frequencias });
      }
      dicionario_guerra_dia.forEach(montaGraficoGuerraDia);
      this.createLineChart(
        "morris-line-example",
        $data,
        "y",
        ["a", "b"],
        ["Participações", "Frequências"],
        ["0.1"],
        ["#fff"],
        ["#000"],
        ["#163282", "#66bb6a"]
      );

      var dicionario_ultimas_siege = JSON_GRAFICO_ULTIMAS_SIEGE;
      var $stckedData = [];
      function montaGraficoUltimasSiege(value, index, array) {
        var participacoes_herois = value.participacoes_herois;
        var frequencias_membros = value.frequencias_membros;
        var dias = value.dia;
        if (participacoes_herois == null) {
          participacoes_herois = 0;
        }
        if (frequencias_membros == null) {
          frequencias_membros = 0;
        }
        $stckedData.push({
          y: dias,
          a: participacoes_herois,
          b: frequencias_membros
        });
      }
      dicionario_ultimas_siege.forEach(montaGraficoUltimasSiege);
      this.createStackedChart(
        "morris-bar-stacked",
        $stckedData,
        "y",
        ["a", "b"],
        ["Heróis", "Membros"],
        ["#9c27b0", "#66bb6a"]
      );

      var dicionario_qtd_classes = JSON_GRAFICO_QTD_CLASSES;
      // var $donutData = [
      //   { label: "Download Sales", value: 12 },
      //   { label: "In-Store Sales", value: 30 },
      //   { label: "Mail-Order Sales", value: 20 }
      // ];
      var $donutData = [];
      var cores = [];
      function montaGraficoQtdClasses(value, index, array) {
        var nome_classe = value.nome;
        var cor = value.cor;
        var numero = value.n;
        if (numero != 0) {
          $donutData.push({
            label: nome_classe,
            value: numero
          });
          cores.push(cor);
        }
      }
      dicionario_qtd_classes.forEach(montaGraficoQtdClasses);
      this.createDonutChart("morris-donut-example", $donutData, cores);
    }),
    //init
    ($.MorrisCharts = new MorrisCharts()),
    ($.MorrisCharts.Constructor = MorrisCharts);
})(window.jQuery),
  //initializing
  (function($) {
    "use strict";
    $.MorrisCharts.init();
  })(window.jQuery);
