var market = require('steam-market-pricing');

var itemName = 'M4A1-S';
var skin = "Decimator";
var state = "(Field-Tested)";
var name = itemName + " | " + skin + " " + state;

market.getItemPrice(730, name, function(err, data) {
    if(!err) {
        if(data == {})
            console.log("fail");
        else
            console.log(data);
    }
});