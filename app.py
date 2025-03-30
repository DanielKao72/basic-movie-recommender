from flask import Flask, render_template, jsonify
from services.Content_Curator import Content_Curator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/movies')
def get_movies():
    """
    Display the catalogue.
    """
    
    # Create an instance of ContentCurator
    content_curator = Content_Curator()
    
    # Get movies from the movies_source (csv).
    possible_movies = Content_Curator.search_movies()
    
    # Create catalogue from all the movies.
    catalogue = Content_Curator.select_movies(possible_movies)
    
    # Return the catalogue as JSON
    return jsonify(catalogue)

if __name__ == '__main__':
    app.run(debug=True)

'''
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Cargar el catálogo de películas
def load_movies():
    df = pd.read_csv('movies.txt', delimiter='|', names=['title', 'genres', 'description'])
    df['features'] = df['genres'] + " " + df['description']
    return df

# Cargar las valoraciones
def load_ratings():
    try:
        return pd.read_csv('ratings.txt', delimiter='|', index_col=0)
    except FileNotFoundError:
        return pd.DataFrame()

movies = load_movies()
vectorizer = TfidfVectorizer(stop_words='english')
feature_matrix = vectorizer.fit_transform(movies['features'])
similarity_matrix = cosine_similarity(feature_matrix)

@app.route('/rate', methods=['POST'])
def rate_movie():
    data = request.json
    username = data['username']
    ratings = data['ratings']  # Diccionario {película: puntuación}

    df_ratings = load_ratings()
    df_ratings.loc[username] = ratings
    df_ratings.to_csv('ratings.txt', sep='|')

    return jsonify({"message": "Ratings saved successfully."})

@app.route('/recommend/<username>', methods=['GET'])
def recommend(username):
    df_ratings = load_ratings()
    
    if username not in df_ratings.index:
        return jsonify({"error": "User not found."})
    
    user_ratings = df_ratings.loc[username].dropna()
    liked_movies = user_ratings[user_ratings >= 4].index.tolist()
    
    if not liked_movies:
        return jsonify({"message": "Not enough ratings to generate recommendations."})
    
    recommended = []
    for movie in liked_movies:
        movie_index = movies[movies['title'] == movie].index[0]
        scores = list(enumerate(similarity_matrix[movie_index]))
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:4]
        recommended += [movies.iloc[i[0]]['title'] for i in sorted_scores]

    return jsonify({"recommendations": list(set(recommended))})

if __name__ == '__main__':
    app.run(debug=True)

'''