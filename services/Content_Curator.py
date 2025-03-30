import pandas as pd

class Content_Curator:
    """
    Content Curator class to handle movie data and catalogues.
    This class is responsible for searching and selecting movies from a dataset.
    """

    def search_movies(movies_source='./data/movies_dataset.csv'):
        """
        Get movies form the movies_source (csv).
        """
        try:
            movies_list = pd.read_csv(movies_source, encoding='latin-1')  # Encoding added if necessary
            
            return movies_list
        except:
            print(f"Error: The file {movies_source} was not found.")
            return []
        

    def select_movies(movies_list):
        """
        Select a catalogue from all the movies.
        """
        size_of_catalogue = 10
        
        catalogue = movies_list.head(size_of_catalogue)
        
        catalogue = catalogue.to_dict(orient='records')
        
        return catalogue