document.getElementById('searchButton').addEventListener('click', function() {
    const searchTerm = document.getElementById('searchInput').value;
    console.log('Search term:', searchTerm);

    fetch('http://127.0.0.1:5001/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'query=' + searchTerm,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Search results:', data);
        const resultsContainer = document.getElementById('resultsContainer');
        if (resultsContainer) {
            resultsContainer.innerHTML = ''; // Clear previous results
            if (data && data.results) {
                data.results.forEach(result => {
                    const resultElement = document.createElement('p');
                    resultElement.innerHTML = `<a href="${result.link}" target="_blank">${result.title}</a><br>${result.content} (Sentiment: ${result.sentiment})`;
                    resultsContainer.appendChild(resultElement);
                });
            } else {
                resultsContainer.innerHTML = '<p>No results found.</p>';
            }
        }
        document.getElementById('searchInput').value = ''; // Clear search input
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
