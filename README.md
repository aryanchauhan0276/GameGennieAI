# GameGennieAI 
Access it here - https://gamegennieai.streamlit.app/
# Problem Statement -  AI-Powered Game Discovery Platform:
Finding the perfect game can be difficult, especially with thousands of titles available across
different platforms. At the same time, creating a custom game often requires programming
skills and game development experience. Advances in Generative AI make it possible to
simplify both game discovery and game creation.
Develop an AI-powered platform that allows users to describe the type of game they want
to play using natural language (e.g., "a multiplayer shooting game with futuristic weapons"
or "a 2D puzzle game with increasing difficulty"). The platform should understand the user's
request, search its game database and online sources to recommend the most relevant
games, and, where feasible, generate a simple playable game based on the user's prompt.
The solution should provide personalized recommendations, an intuitive user experience,
and support a wide variety of game genres and play styles.

# Solution -  GameGennieAI
This solution address the problem statement by utilizing open source libraries & models available. This solution takes the dataset from Kaggle mentioned as “playstore_games_with_descriptions.csv” which consists over 15000+ recrords. Then, continues to use sentence transformers available on hugging face to embedded the text into numericals and then these numericals are scaled down using the FAISS library from facebook to optimize the model.
The user input is embedded using the same hugging face transformers and using semantic search and Keybert the recommendation is generated.

# *Tech Stack-*
o	Sentence Transformers – Hugging Face
o	FAISS – Facebook
o	StreamLit
o	Google Colab
o	Kaggle Dataset
o	Pandas
o	Numpy

# *The Models –*
Dataset – Kaggle 
To date (April 2020), Android is still the most popular mobile operating system in the world. Taking into account billion of Android users worldwide, mining this data has the potential to reveal user behaviors and trends in the whole global scope.


*Sentence Transformer all-MiniLM-L6-v2- Hugging Face*
This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search. 
Usage (HuggingFace Transformers)
Without sentence-transformers, you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

*FAISS*
FAISS (Facebook AI Similarity Search) is an open-source library developed by Meta AI (FAIR) designed for efficient similarity search and clustering of dense vectors. AISS solves this by organizing vectors into specialized data structures called indexes, allowing applications to rapidly retrieve the most similar items (nearest neighbors) from millions or billions of data points—even when the data exceeds RAM capacity. It is widely used in semantic search, recommendation systems, and giving long-term memory to large language models (RAG pipelines).

*Streamlit*
Streamlit is an open-source Python framework used to build and deploy interactive web applications rapidly. It allows developers to create clean, responsive frontends entirely in Python without needing HTML, CSS, or JavaScript.



# Process
Dataset from Kaggle is being used by the team for model training and raw data source. As every raw data have some null values, repeated rows and missing columns, the data cleaning is done via Pandas and Numpy  and a column named description has been added via Claude which consists of the description, type and the age category. These name and description columns are combined to form new column named “AppDetails” which will further make the search task easier. Then, sentence transformers are used to convert the text details into numericals which afterwards are normalized using FAISS to optimize the model and increase its computational speed. After that the user provides the input based on their requirements and the model computes them into numericals after that the model using semantic search to return the top 5 games based on the users requirements .
