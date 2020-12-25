// json data
//function fetchMetadata(sample) {
    //d3json('/metadata/${sample').then((data) => {

        //var PANEL = d3.select('#sample-metadata');

        //PANEL.html("");

        //Object.entries(data).forEach(([key, value]) => {
            //PANEL.append("h5").text('${key}: ${value');
        //});

        //Bonus- for guage chart

        //fetchGuage(data.WFREQ);

    //});
    
//}

//Bar chart

function barChart(sample) {
    d3.json('samples.json').then((data) => {
        console.log(data);
     var oneSample =   data.samples.filter(sampleId => sampleId.id == sample)[0]
        var ids = oneSample.otu_ids.map(otuID => `OTU ${otuID}`).slice(0, 10).reverse();
        var labels = oneSample.otu_labels.slice(0, 10).reverse();
        var values = oneSample.sample_values.slice(0, 10).reverse();

        var trace1 = {
            x: values,
            y: ids,
            type: "bar",
            orientation: "h"            
        };
        
        var data = [trace1];
        
        var layout = {
            title: "Belly Button Bar Chart",
            xaxis: {title: "ids"},
            yaxis: {title: "Sample Values"}
        }
        
        Plotly.newPlot("bar", data, layout);


    });
};  

function optionChanged (sampleId) {
    barChart(sampleId)
}

function init() {
    barChart(940)



}

init()

