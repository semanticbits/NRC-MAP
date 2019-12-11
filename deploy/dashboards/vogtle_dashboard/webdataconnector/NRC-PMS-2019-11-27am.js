(function() {
    var myConnector = tableau.makeConnector();

    myConnector.getSchema = function (schemaCallback) {
        var cols = [
            { id: "date", alias: "date", dataType: tableau.dataTypeEnum.string },
            { id: "starttime", alias: "starttime", dataType: tableau.dataTypeEnum.string },
            { id: "endtime", alias: "endime", dataType: tableau.dataTypeEnum.string },
            { id: "purpose", alias: "purpose", dataType: tableau.dataTypeEnum.string },
            { id: "location", alias: "location", dataType: tableau.dataTypeEnum.string },
            { id: "contact", alias: "contact", dataType: tableau.dataTypeEnum.string }
        ];

        var tableSchema = {
            id: "pms",
            alias: "Public Meeting Schedule for NRC",
            columns: cols
        };

        schemaCallback([tableSchema]);
    };


    myConnector.getData = function (table, doneCallback) {
        var connectionUrl = "PMShtml.html";
        var xhr = $.ajax({
            url : connectionUrl,
            cache: false,
            success: function (response) {
                var pmsTableRows = $(response).find('tr');

                // Skipping first three rows inefficiently 
                pmsTableRows = pmsTableRows.not(':first'); 
                pmsTableRows = pmsTableRows.not(':first'); 
                pmsTableRows = pmsTableRows.not(':first');
                pmsTableRows = pmsTableRows.not(':last'); 

                var tableData = [];
                pmsTableRows.each(function (i, row) {
                    var $pmsTableColumnsInRow = $(this).find('td');
                    var date = $($pmsTableColumnsInRow[0]).text().match(/\d{2}\/\d{2}\/\d{2}/);
                    var $time = $($pmsTableColumnsInRow[0]).text().match(/\d{1,2}:\d{2}[A-Z]{2}/g)
                    var starttimestring = $time[0];
                    var endtimestring = $time[1];
                    console.log("purpose");
                    console.log($($pmsTableColumnsInRow[1]).text());
                    console.log("purpose link");
                    console.log($($pmsTableColumnsInRow[1]).find('a');
                    var purposeLink = $($pmsTableColumnsInRow[1]).find('a');
                    //console.log("location location location");
                    //console.log($($pmsTableColumnsInRow[2]).text());
                    //console.log("That's the contact");
                    //console.log($($pmsTableColumnsInRow[3]).text());
                    // Build a row from the parsed response
                    tableData.push({
                        'date':  $($pmsTableColumnsInRow[0]).text().match(/\d{2}\/\d{2}\/\d{2}/),
                        'starttime': starttimestring,
                        'endtime': endtimestring,
                        'purpose': $($pmsTableColumnsInRow[1]).text(),
                        'location': $($pmsTableColumnsInRow[2]).text(),
                        'contact': $($pmsTableColumnsInRow[3]).text()
                    });

                });

                    table.appendRows(tableData);
                    doneCallback();
                }});
    };
    tableau.registerConnector(myConnector);
    

    $(document).ready(function () {
        $("#submitButton").click(function () {
            tableau.connectionName = "Public Meeting Schedule Feed";
            tableau.submit();
        });
    });
})();