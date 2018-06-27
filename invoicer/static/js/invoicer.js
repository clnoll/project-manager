function calculateCost(item_id) {
    var rate = parseFloat(document.getElementById("taskitem_rate_" + item_id).value);
    var minutes_billed = parseFloat(document.getElementById("taskitem_minutes_billed_" + item_id).value);
    document.getElementById("taskitem_cost_" + item_id).innerHTML = "$" + Math.round(rate * minutes_billed / 60).toFixed(2);
};


function calculateAllCosts() {
    var taskitems = document.getElementsByClassName("taskitem");
    [].forEach.call(taskitems, function(taskitem) {
	calculateCost(taskitem.id);
    })
};


window.onload = function() {
    calculateAllCosts();
};
