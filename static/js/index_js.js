document.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("/api/movies");
    const movies = await response.json();
    const container = document.getElementById("movies-container");

    movies.forEach(movie => {
        const movieDiv = document.createElement("div");
        movieDiv.classList.add("movie-card");

        const select = document.createElement("select");
        select.classList.add("rating");

        select.innerHTML = `
            <option value="">No rate</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
        `;

        movieDiv.innerHTML = `
            <h3>${movie.title}</h3>
            <p class="description">${movie.description}</p>
        `;

        movieDiv.appendChild(select);
        container.appendChild(movieDiv);

        // Event listener to add/remove the "rated" class
        select.addEventListener("change", function () {
            if (select.value !== "") {
                movieDiv.classList.add("rated");
            } else {
                movieDiv.classList.remove("rated");
            }
        });
    });
});
   
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("submit-button").addEventListener("click", async () => {
        const username = document.getElementById("username").value.trim();
    
        if (!username) {
            alert("Please enter your username before submitting the ratings.");
            return;
        }
    
        const ratingElements = document.querySelectorAll(".movie-card");
        const ratings = Array.from(ratingElements).map(movieDiv => {
            const title = movieDiv.querySelector("h3").innerText;
            const rating = movieDiv.querySelector(".rating").value || 0;
            return { title, rating: parseInt(rating) };
        });
    
        try {
            const response = await fetch("/api/rate_movies", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ username, ratings })
            });
    
            if (response.ok) {
                alert("Rates successfully submitted.");
            } else {
                alert("Unsuccessfully submitted.");
            }
        }
        catch (error) {
            console.error("Error submitting ratings:", error);
            alert("Error submitting ratings. Please try again.");
        }
    });
});