document.addEventListener('DOMContentLoaded', function() {

    // Function to sort results
    function sortResults(results, sortBy) {
        //sort by sentiments
        if (sortBy === 'sentiment') {
            return results.sort((a, b) => {
                const sentimentA = Math.round((a.score[0] + 1) * 50);
                const sentimentB = Math.round((b.score[0] + 1) * 50);
                return sentimentB - sentimentA;
            });

            //sort by subjectivity
        } else if (sortBy === 'subjectivity') {
            return results.sort((a, b) => {
                const subjectivityA = Math.round(a.score[1] * 100);
                const subjectivityB = Math.round(b.score[1] * 100);
                return subjectivityB - subjectivityA;
            });
        }
        return results;
    }

    let currentResults = []; // Store current results globally

    // Handle search button click
    document.getElementById('searchButton').addEventListener('click', function(event) {
        event.preventDefault();
        const query = document.getElementById('searchQuery').value.trim().toLowerCase();
        
        if (query === '') {
            alert("Please enter a search term.");
            return;
        }

        // Show loading spinner
        document.getElementById('loadingSpinner').style.display = 'flex';
        // Hide previous results if any
        document.getElementById('results').style.display = 'none';

        //GET REQUEST 
        url = `../search?q=${query}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                searchResults = data;
                console.log(searchResults);
                // Hide spinner
                document.getElementById('loadingSpinner').style.display = 'none';
                document.getElementById('results').style.display = 'block';
                
                // Filter results
                currentResults = searchResults.filter(result => {
                    return result.status && (
                        result.title.toLowerCase().includes(query) ||
                        result.snippet.toLowerCase().includes(query)
                    );
                });

                // Display with current sort option
                const sortBy = document.getElementById('sortFilter').value;
                displayResults(currentResults, sortBy, query);
            })
            .catch(error => {
                console.error('Error fetching searchResults:', error);
                // Hide spinner on error
                document.getElementById('loadingSpinner').style.display = 'none';
                document.getElementById('results').style.display = 'block';
            });
    });

    // Handle sort filter changes
    document.getElementById('sortFilter').addEventListener('change', function(e) {
        if (currentResults.length > 0) {
            const query = document.getElementById('searchQuery').value.trim().toLowerCase();
            displayResults(currentResults, e.target.value, query);
        }
    });

    function displayResults(results, sortBy = 'sentiment', query = '') {
        const resultsContainer = document.getElementById('results');
        resultsContainer.innerHTML = '';

        // Sort the results
        const sortedResults = sortResults([...results], sortBy);
        //
        if (sortedResults.length === 0) {
            const noResultsElement = document.createElement('div');
            noResultsElement.classList.add('no-results');
            noResultsElement.innerHTML = `<p>No results found for "${query}"</p>`;
            resultsContainer.appendChild(noResultsElement);
            return;
        }

        // Display results
        sortedResults.forEach(result => {
            const resultElement = document.createElement('div');
            resultElement.classList.add('result-item');
            
            const sentimentScore = result.score[0];
            const sentimentPercent = Math.round((sentimentScore + 1) * 50);
            
            const subjectivityScore = result.score[1];
            const subjectivityPercent = Math.round(subjectivityScore * 100);
            
            const sentimentClass = sentimentScore > 0.3 ? 'positive' : 
                                 sentimentScore < -0.3 ? 'negative' : 'neutral';
            
            resultElement.innerHTML = `
                <h3>${result.title}</h3>
                <p class="snippet">${result.snippet}</p>
                <div class="scores-container">
                    <div class="sentiment-score ${sentimentClass}">
                        <span class="score-label">Sentiment:</span>
                        <span class="score-value">${sentimentPercent}%</span>
                    </div>
                    <div class="subjectivity-score">
                        <span class="score-label">Subjectivity:</span>
                        <span class="score-value">${subjectivityPercent}%</span>
                    </div>
                </div>
                <a href="${result.url}" target="_blank">Read more</a>
            `;
            
            resultsContainer.appendChild(resultElement);
        });

        // Scroll to results
        document.getElementById('results').scrollIntoView({ 
            behavior: 'smooth',
            block: 'start'
        });
    }

    // Handle info popup
    const infoBtn = document.getElementById('infoBtn');
    const infoPopup = document.getElementById('infoPopup');
    const closeBtn = document.querySelector('.close-btn');

    // Add console logs to debug
    infoBtn.addEventListener('click', () => {
        console.log('Info button clicked');
        infoPopup.classList.add('show');
        console.log('Added show class');
    });

    closeBtn.addEventListener('click', () => {
        console.log('Close button clicked');
        infoPopup.classList.remove('show');
    });

    // Close popup when clicking outside
    document.addEventListener('click', (e) => {
        if (!infoPopup.contains(e.target) && !infoBtn.contains(e.target)) {
            infoPopup.classList.remove('show');
        }
    });

    // Add this with your other event listeners
    const howItWorksBtn = document.getElementById('howItWorksBtn');
    const howItWorksDropdown = document.getElementById('howItWorksDropdown');

    howItWorksBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        howItWorksDropdown.classList.toggle('show');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!howItWorksBtn.contains(e.target) && !howItWorksDropdown.contains(e.target)) {
            howItWorksDropdown.classList.remove('show');
        }
    });
});
