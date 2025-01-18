document.addEventListener('DOMContentLoaded', function() {

    // Handle search button click
    document.getElementById('searchButton').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent page reload on form submission
        
        const query = document.getElementById('searchQuery').value.trim();
        console.log("Search button clicked");

        // Ensure the query is not empty
        if (query === '') {
            alert("Please enter a search term.");
            return;
        }

        console.log(`Searching for: ${query}`);  // Log query for debugging

        // Clear previous results
        document.getElementById('results').innerHTML = '';

        // Simulate search results with sentiment analysis
        const simulatedResults = [ 
            { title: "Positive Review of HAHA Product A", link: "#", sentiment: 0.8 },
            { title: "Inspirational Story A  HAHA About Overcoming Challenges", link: "#", sentiment: 0.9 },
            { title: "Clickbait Article A  HAHA on Controversy", link: "#", sentiment: -0.5 },
            { title: "Positive Review of HAHA Product A", link: "#", sentiment: 0.8 },
            { title: "Inspirational Story A  HAHA About Overcoming Challenges", link: "#", sentiment: 0.9 },
            { title: "Clickbait Article A  HAHA on Controversy", link: "#", sentiment: -0.5 },
            { title: "Positive Review of HAHA Product A", link: "#", sentiment: 0.8 },
            { title: "Inspirational Story A  HAHA About Overcoming Challenges", link: "#", sentiment: 0.9 },
            { title: "Clickbait Article A  HAHA on Controversy", link: "#", sentiment: -0.5 },
            { title: "Positive Review of HAHA Product A", link: "#", sentiment: 0.8 },
            { title: "Inspirational Story A  HAHA About Overcoming Challenges", link: "#", sentiment: 0.9 },
            { title: "Clickbait Article A  HAHA on Controversy", link: "#", sentiment: -0.5 },
            { title: "Positive Review of HAHA Product A", link: "#", sentiment: 0.8 },
            { title: "Inspirational Story A  HAHA About Overcoming Challenges", link: "#", sentiment: 0.9 },
            { title: "Clickbait Article A  HAHA on Controversy", link: "#", sentiment: -0.5 },
            { title: "Positive Review of HAHA Product A", link: "#", sentiment: 0.8 },
            { title: "Inspirational Story A  HAHA About Overcoming Challenges", link: "#", sentiment: 0.9 },
            { title: "Clickbait Article A  HAHA on Controversy", link: "#", sentiment: -0.5 },
            { title: "Positive Review of HAHA Product A", link: "#", sentiment: 0.8 },
            { title: "Inspirational Story A  HAHA About Overcoming Challenges", link: "#", sentiment: 0.9 },
            { title: "Clickbait Article A  HAHA on Controversy", link: "#", sentiment: -0.5 },
            { title: "Neutral Review of Service B", link: "#", sentiment: 0.1 }
        ];

        // Filter results based on the query (this can be customized)
        const filteredResults = simulatedResults.filter(result => result.title.toLowerCase().includes(query.toLowerCase()));

        // Sort results by sentiment (highest first)
        filteredResults.sort((a, b) => b.sentiment - a.sentiment);

        // Display the results
        const resultsContainer = document.getElementById('results');
        filteredResults.forEach(result => { //iterate through each result 
            const resultElement = document.createElement('div');
            resultElement.classList.add('result-item');
            resultElement.innerHTML = `
                <h3>${result.title}</h3>
                <a href="${result.link}" target="_blank">Read more</a>
            `;
            resultsContainer.appendChild(resultElement);
        });

        // If no results match the query
        if (filteredResults.length === 0) {
            const noResultsElement = document.createElement('div');
            noResultsElement.classList.add('no-results');
            noResultsElement.innerHTML = `<p>No results found for "${query}"</p>`;
            resultsContainer.appendChild(noResultsElement);
        }
    });
});
