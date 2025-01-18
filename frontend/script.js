function handleSearchClick() {
    console.log('Search button clicked via onclick!');
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchButton').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default form submission
        console.log('Search button clicked!');
    });
});
