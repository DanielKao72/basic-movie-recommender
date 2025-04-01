import numpy as np
import csv
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class Recommender:
    def __init__(self):
        self.peliculas = []
        self.peliculas_data = []
        self.usuarios = []
        self.ratings_matrix = None
        self.similarity_matrix = None
        self._load_data()
        self._calculate_similarity()

    def _load_data(self):
        # Load movies
        with open("./data/movies_dataset.csv", 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 2:
                    self.peliculas_data.append({"pelicula": row[0], "descripcion": row[1]})
                    self.peliculas.append(row[0])
        
        # Load user ratings
        data = []
        with open("user_reviews_report.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.usuarios.append(row[0])
                data.append([int(x) for x in row[1:]])
        
        self.ratings_matrix = np.array(data)

    def _calculate_similarity(self):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(pd.DataFrame(self.peliculas_data)["descripcion"])
        self.similarity_matrix = cosine_similarity(tfidf_matrix)

    def recommend_movies(self, usuario):
        if usuario not in self.usuarios:
            return {"error": "Usuario no encontrado"}

        target_user_idx = self.usuarios.index(usuario)
        peliculas_favoritas = np.where(self.ratings_matrix[target_user_idx] >= 3)[0]

        if len(peliculas_favoritas) == 0:
            return {"error": "No hay suficientes películas calificadas para recomendar"}

        missing_movies = np.arange(21, min(len(self.peliculas), 3001))
        predictions = {}

        for movie_idx in missing_movies:
            sim_sum = sum(self.similarity_matrix[movie_idx, fav_idx] for fav_idx in peliculas_favoritas)
            count = len(peliculas_favoritas)
            if count > 0:
                predictions[movie_idx] = sim_sum / count  # Store index instead of title

        recommended_movies = sorted(predictions.items(), key=lambda x: x[1], reverse=True)[:10]

        # Include descriptions using correct indexing
        recomendaciones = [
            {
                "pelicula": self.peliculas[idx],  # Get title
                "descripcion": next((p["descripcion"] for p in self.peliculas_data if p["pelicula"] == self.peliculas[idx]), "Descripción no disponible"),  
                "similitud": round(score, 2)
            } 
            for idx, score in recommended_movies
        ]

        return {"usuario": usuario, "recomendaciones": recomendaciones}

