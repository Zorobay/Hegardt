/**
 * A function used by the global search bar to trigger searches in the Person database
 * @param arg the search term as a string
 */
var showResults = function (arg) {
    const value = arg.trim();

    if (value == "" || value.length <= 0) {  // Empty search string, return
        $("#searchResults").fadeOut();
        return;
    } else {
        $("#searchResults").fadeIn();
        $.get("/search/" + value, function () {
            $("#searchResults").html("");  // Clean up search results
        }).done(function (data) {
            data.forEach(p => {
                $("#searchResults").append(`<li role="presentation"><a role="menuitem" tabindex="-1" href="/ansedel/${p._id}">${p.full_name} [${p.birth_date_pretty}]</a></li>`);
            });
            console.log("Recieved data: " + data);
        });
    }
}
