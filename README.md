---
title: FASHIO
emoji: 🎩
colorFrom: purple
colorTo: purple
sdk: streamlit
sdk_version: 1.36.0
app_file: python main.py
pinned: false
---

# FASHIO 

**About:**
FASHIO is an intelligent fashion recommendation system designed to help users discover the perfect products based on their unique preferences. By leveraging the power of advanced natural language processing and similarity search techniques, FASHIO provides tailored fashion suggestions from a dataset of product descriptions.

**Key Features:**
1. **User-Friendly Interface:** The application features an intuitive and visually appealing user interface built with Streamlit, making it easy for users to input their fashion preferences and receive personalized recommendations.
   
2. **Advanced Embedding Model:** Utilizing the SentenceTransformer model, FASHIO converts product descriptions into high-dimensional embeddings that capture the semantic meaning of each description.

3. **Efficient Similarity Search:** FAISS (Facebook AI Similarity Search) is employed to perform fast and accurate similarity searches over the product embeddings. This ensures that users receive the most relevant product suggestions based on their input.

4. **Real-Time Recommendations:** Users can input their fashion preferences through a simple text box, select the number of recommendations they desire, and receive instant results. The results include product names, descriptions, URLs for direct purchase, and a similarity score indicating how closely each product matches the user’s input.

**How It Works:**
- **Data Preparation:** Product descriptions are preprocessed and encoded into embeddings using a pre-trained SentenceTransformer model.
- **Indexing:** These embeddings are stored in a FAISS index, enabling efficient similarity searches.
- **User Input:** Users provide their fashion preferences through the interface.
- **Query Processing:** The input is encoded into an embedding and compared against the indexed product embeddings using FAISS.
- **Results Display:** The top matching products are displayed, complete with links and similarity scores, allowing users to explore and purchase their desired items.

**Technology Stack:**
- **SentenceTransformer:** For converting textual descriptions into embeddings.
- **FAISS:** For performing fast similarity searches on the embeddings.
- **Streamlit:** For building the user interface and handling user interactions.
- **Pandas:** For data manipulation and management.

FASHIO combines state-of-the-art machine learning techniques with a user-friendly interface to provide personalized fashion recommendations. Whether you’re looking for the latest trends or specific fashion items, FASHIO tailors its suggestions to match your unique style and preferences.

## Dataset 
To scrape quality clothing data containing proper description and url for the product I used `Apify's` [Amazon Product Scraper](https://blog.apify.com/step-by-step-guide-to-scraping-amazon/#step-1-go-to-amazon-product-scraper-on-apify-store)
By creating an account and logging into the console we can input links of the amazon fashion category like- `Men's Fashion -> Shirts`

I downloaded all the scraped data for various clothing categories into a CSV file with columns `url|title|description`

My Apify Console
![Apify Console](https://github.com/jhaayush2004/Fashio/blob/main/Visuals/apifyGh.png)

The full data consists about 3000 different fashion products of men and women, it can be found at [dataset](https://github.com/jhaayush2004/Fashio/blob/main/clothing_similarity_search.csv).

## Data Cleaning
I used `pandas` to clean the data and preprocess the text data by cleaning it (remove special characters, lowercasing, etc.), and possibly by applying text normalization .

## Designing Finetuning Dataset
I designed a finetuning dataset containing about 30-35 product details in the format `Input query| product title| Label` , where "Label" is the matching score between "Input query" & "product title".
This dataset can be found at [finetuning dataset](https://github.com/jhaayush2004/Fashio/blob/main/finetuning_data.csv).

## Model
The base model used is `sentence-transformers/all-MiniLM-L6-v2` from Huggingface. This huggingface model has then been finetuned on the `finetuning_data.csv` to improve model's performance on our dataset.The choice of this model selection was based on its small size and good accuracy.
So, the final finetuned model that has been used is `ShauryaNova/autotrain-rp16o-pxwa0`.
![App Screenshot](https://github.com/jhaayush2004/Fashio/blob/main/Visuals/huggingfac.png)

## Generating Embeddings
`sentence-transformers` has been used to make embeddings for the cleaned data. I used `all-MiniLM-L6-v2` model to make the embeddings. The model card can be found [here](https://huggingface.co/ShauryaNova/autotrain-rp16o-pxwa0) .

First install the Sentence Transformers library:

```pip install -U sentence-transformers```

Then we can load the model

```py
from sentence_transformers import SentenceTransformer

# Download from the Hugging Face Hub
model = SentenceTransformer("ShauryaNova/autotrain-rp16o-pxwa0")
# Run inference
sentences = [
    'search_query: autotrain',
    'search_query: auto train',
    'search_query: i love autotrain',
]
embeddings = model.encode(sentences)

```
The ```product_embeddings.index``` file serves as the index structure used for efficient similarity search operations in FASHIO. It stores precomputed embeddings in a format that enables rapid retrieval of similar fashion products based on user queries. This index file optimizes the search process by organizing embeddings in a way that facilitates quick comparison and retrieval, enhancing the responsiveness and performance of the recommendation system.

## API
FASHIO utilizes FAISS to enable an API endpoint /predict that accepts a query string and retrieves the top N most similar fashion products as JSON. This endpoint leverages FAISS for efficient similarity search operations, allowing users to receive tailored fashion product recommendations based on their input queries.

Example Usage:

Send a POST request to http://0.0.0.0:8080/predict with a JSON payload like:

```py
{
    "query": "Men's winter jacket black and white"
}
```

This will return a JSON response with URLs of similar fashion products:

```py
{
  "similar_urls": [
    "https://www.amazon.in/dp/B082L3BGGM",
    "https://www.amazon.in/dp/B08KWFRY6W",
    "https://www.amazon.in/dp/B08Q3VBFPD",
    "https://www.amazon.com/dp/B07S1LMK58",
    "https://www.amazon.in/dp/B0B8YY38VF"
  ]
}
```
![App Screenshot](https://github.com/jhaayush2004/Fashio/blob/main/Visuals/fashishot.png)
## Running Locally
- Clone the repo
- Make a virtual environment
- Install the dependencies `pip install -r requirements.txt`
- Run the server `python main.py`

## Do Visit

- Live Demo Video of Model : [Youtube](https://youtu.be/5Rgm-8wLJ0A)
- Visit my finetuned model at [ShauryaNova/autotrain-rp16o-pxwa0](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
