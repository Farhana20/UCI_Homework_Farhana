// from data.js
var tableData = data;


// YOUR CODE HERE!
var tbody = d3.select("tbody");

//console.log(tableData);
tableData.forEach(function(UFOSightings) {

    console.log(UFOSightings);
    var row = tbody.append("tr");

    Object.entries(UFOSightings).forEach(function([key, value]){
        console.log(key, value);

        var cell = row.append("td");
        cell.text(value);

    });
    
     

});
    
    