$(document).ready(function () {
    // Function to fetch and display filtered data
    function fetchData() {
        var keyword = $('#keyword').val();
        var model = $('#model').val();

        $.ajax({
            url: '/filtered_data',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({keyword: keyword, model: model}),
            success: function (response) {
                var tbody = $('#data-body');
                tbody.empty();
                response.forEach(function (row) {
                    tbody.append('<tr>' +
                        '<td>' + row.date + '</td>' +
                        '<td>' + row.keyword_id + '</td>' +
                        '<td>' + row.model + '</td>' +
                        '<td>' + row.domain + '</td>' +
                        '<td>' + row.position + '</td>' +
                        '</tr>');
                });
            },
            error: function (xhr, status, error) {
                console.error('Error fetching data:', error);
            }
        });
    }

    // Call fetchData function when filter button is clicked
    $('#filter-btn').click(fetchData);

    // Initial data fetch when the page loads
    fetchData();
});
