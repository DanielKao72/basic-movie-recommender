import csv
import os

class Movie_Reviewer:

    def add_user_review(username, movie_titles, ratings, report="user_reviews_report.csv"):
        """
        Add a review for the movie.
        """
        with open(report, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not os.path.isfile(report):
                writer.writerow(["Username"] + movie_titles)
                
            writer.writerow([username] + ratings)
                
    def is_registered_user(username, report="user_reviews_report.csv"):
        """
        Check if the user is registered.
        """
        with open(report, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    return True
        return False
    
    def update_user_review(username, movie_title, rating, report="user_reviews_report.csv"):
        """
        Update the review for the movie.
        """
        with open(report, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        for i, row in enumerate(rows):
            if row[0] == username:
                rows[i] = [username] + rating
                break
        
        with open(report, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            
    def get_all_usernames(report="user_reviews_report.csv"):
        """
        Get all usernames from the report.
        """
        usernames = set()
        with open(report, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != "Username":
                    usernames.add(row[0])
        return list(usernames)
        