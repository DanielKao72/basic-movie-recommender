from flask import Flask, render_template, jsonify, request
from services.Content_Curator import Content_Curator
from services.Movie_Reviewer import Movie_Reviewer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/movies')
def get_movies():
    """
    Display the catalogue.
    """
    # Get movies from the movies_source (csv).
    possible_movies = Content_Curator.search_movies()
    
    # Create catalogue from all the movies.
    catalogue = Content_Curator.select_movies(possible_movies)
    
    # Return the catalogue as JSON
    return jsonify(catalogue)

@app.route('/api/rate_movies', methods=['POST'])
def save_rating_movies():
    data = request.get_json()
    
    username = data.get('username')
    ratings = data.get('ratings')
    
    movie_titles = [movie['title'] for movie in ratings]
    ratings_values = [movie['rating'] for movie in ratings]
    
    # Check if the user is registered
    if not Movie_Reviewer.is_registered_user(username):
        Movie_Reviewer.add_user_review(username, movie_titles, ratings_values)
    else:
        Movie_Reviewer.update_user_review(username, movie_titles, ratings_values)
    
    return jsonify({"message": "Rating received!"})

if __name__ == '__main__':
    app.run(debug=True)