$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });

});

function print_result(results) {
console.log(results);
$("#Results").empty();
results.forEach(game => {
const template = `
            <div class="col-4 mb-3">
                <div class="card">
                    <div class="card-header">
                      ${game.name}
                    </div>
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item">Rating: ${game.average_rating}/10</li>
                      <li class="list-group-item">Age: ${game.binned_min_age}</li>
                      <li class="list-group-item">Players: ${game.min_players} - ${game.max_players}</li>
                      <li class="list-group-item">Playtime: ${game.binned_playtime}</li>
                      <li class="list-group-item">Category: ${game.binned_category}</li>
                      <li class="list-group-item">Mechanics: ${game.binned_mechanics}</li>
                    </ul>
                  </div>
            </div>
`
$("#Results").append(template);
});  
}

// call Flask API endpoint
function makePredictions() {
    var name = $("#name").val();
    var age = $("#age").val();
    var min_playtime = $("#min_playtime").val();
    var max_playtime = $("#max_playtime").val();
    var min_players = $("#min_players").val();
    var max_players = $("#max_players").val();
    var avg_rating = $("#avg_rating").val();


    // check if inputs are valid

    // create the payload
    var payload = {    
            "name": name,
            "min_players": min_players,
            "max_players": max_players,
            "min_playtime": min_playtime,
            "max_playtime": max_playtime,    
            "min_age": age,
            "min_average_rating": avg_rating,
        }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/predictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            // console.log(returnedData);
            
            if (returnedData["ok"]  ) {
                $("#output").text("Results Below");
                print_result(returnedData.prediction)
            } else {
                $("#output").text("Something went wrong...");
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}