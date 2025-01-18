document.addEventListener('DOMContentLoaded', function() {
    // Sample search results data, replace with actual data later 
    const searchResults = [
        {
            "url": "https://www.nytimes.com/2025/01/17/opinion/marc-andreessen-trump-silicon-valley.html",
            "title": "Opinion | How Democrats Drove Silicon Valley Into Trump's Arms ...",
            "score": [
                0.0,
                0.0
            ],
            "snippet": "1 day ago ... How Democrats Drove Silicon Valley Into Trump's Arms. Marc Andreessen explains the newest faction of conservatism. Jan. 17, 2025.",
            "status": false
        },
        {
            "url": "https://www.fmprc.gov.cn/eng/xw/zyxw/202501/t20250117_11538172.html",
            "title": "President Xi Jinping Speaks with U.S. President-Elect Donald J ...",
            "score": [
                0.2387657058388766,
                0.4471182273011541
            ],
            "snippet": "1 day ago ... President Xi congratulated Trump on his reelection as President of the United States. President Xi noted that they both attach great importance...",
            "status": true
        },
        {
            "url": "https://www.nytimes.com/interactive/2025/01/17/us/trump-president-reaction.html",
            "title": "Readers Share Their Inner Thoughts Ahead of Trump's Second ...",
            "score": [
                0.0996332972582973,
                0.47531836219336204
            ],
            "snippet": "20 hours ago ... The Inner Thoughts of a Nation Heading Into the Next Trump Era. By The New York Times. Jan. 17, 2025.",
            "status": true
        },
        {
            "url": "https://www.aol.com/trump-promised-mass-deportations-one-110000027.html",
            "title": "How Trump could supercharge the deportation pipeline | The Texas ...",
            "score": [
                0.02319772064670024,
                0.37414745118826737
            ],
            "snippet": "1 day ago ... Trump promised mass deportations. Here's one way they could quietly ... Trump hasn't elaborated on his plan, but immigration attorneys...",
            "status": true
        },
        {
            "url": "https://www.cnn.com/2025/01/17/politics/inauguration-moving-indoors-cold-weather/index.html",
            "title": "Trump's inauguration to be moved indoors | CNN Politics",
            "score": [
                -0.033138435638435645,
                0.4696169571169571
            ],
            "snippet": "18 hours ago ... President-elect Donald Trump's inauguration will be moved indoors, he announced Friday, due to dangerously cold temperatures projected in...",
            "status": true
        }
    ];
    // Function to sort results
    function sortResults(results, sortBy) {
        //sort by sentiments
        if (sortBy === 'sentiment') return results.sort((a, b)=>{
            const sentimentA = Math.round((a.score[0] + 1) * 50);
            const sentimentB = Math.round((b.score[0] + 1) * 50);
            return sentimentB - sentimentA;
        });
        else if (sortBy === 'subjectivity') return results.sort((a, b)=>{
            const subjectivityA = Math.round(a.score[1] * 100);
            const subjectivityB = Math.round(b.score[1] * 100);
            return subjectivityB - subjectivityA;
        });
        return results;
    }
    let currentResults = []; // Store current results globally
    // Handle search button click
    document.getElementById('searchButton').addEventListener('click', function(event) {
        event.preventDefault();
        //get search query and filter results (trim and lower)
        const query = document.getElementById('searchQuery').value.trim().toLowerCase();
        //check if search query is empty
        if (query === '') {
            alert("Please enter a search term.");
            return;
        }
        // Filter results
        currentResults = searchResults.filter((result)=>{
            return result.status && (result.title.toLowerCase().includes(query) || result.snippet.toLowerCase().includes(query));
        });
        // Display with current sort option
        const sortBy = document.getElementById('sortFilter').value;
        displayResults(currentResults, sortBy, query);
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
        const sortedResults = sortResults([
            ...results
        ], sortBy);
        //
        if (sortedResults.length === 0) {
            const noResultsElement = document.createElement('div');
            noResultsElement.classList.add('no-results');
            noResultsElement.innerHTML = `<p>No results found for "${query}"</p>`;
            resultsContainer.appendChild(noResultsElement);
            return;
        }
        // Display results
        sortedResults.forEach((result)=>{
            const resultElement = document.createElement('div');
            resultElement.classList.add('result-item');
            const sentimentScore = result.score[0];
            const sentimentPercent = Math.round((sentimentScore + 1) * 50);
            const subjectivityScore = result.score[1];
            const subjectivityPercent = Math.round(subjectivityScore * 100);
            const sentimentClass = sentimentScore > 0.3 ? 'positive' : sentimentScore < -0.3 ? 'negative' : 'neutral';
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
});

//# sourceMappingURL=index.5e469f4a.js.map
