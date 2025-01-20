# Feeltr for UoftHacks 12
**Feeltr (Feel + Filter) - Feel the Search, Not Just the Clicks**  

**Try it out:** [Feeltr](https://feeltr.onrender.com/static/index.html)

![Feeltr.png](https://ibb.co/9qGTvB5)

## Description
Instead of ranking results based on popularity, interactions, or SEO tactics, Feeltr prioritizes content that is the least subjective and least polarizing. This ensures that users are presented with reliable, emotionally neutral, and meaningful results.
`
With Feeltr, we aim to create a search experience that’s aligned with human needs—providing clarity, positivity, and relevance every time you search.

Type in any prompt, and Feeltr will analyze search results for sentiment and subjectivity to help you find accurate and positive information.  
## 🛠️ Technologies Used  
### Backend:  
- Python  
  - Flask  
  - Google Custom Search JSON API  
  - BeautifulSoup 4  
  - TextBlob  

### Frontend:  
- JavaScript  
- HTML  
- CSS

## 🚀 How It Works  
1. **Data Gathering**:  
   - Uses Google Custom Search JSON API to fetch search results.  

2. **Content Parsing**:  
   - BeautifulSoup 4 parses and extracts relevant data from the search results.  

3. **Sentiment & Subjectivity Analysis**:  
   - TextBlob analyzes each result's content to generate scores for:  
     - **Positivity**: Measures how positive the content is.  
     - **Subjectivity**: Evaluates how objective or biased the content is.  

4. **Ranking**:  
   - Results are ranked based on emotional neutrality and reliability.
   - Sort features: sort by subjectivity and sort by positivity.  
