document.addEventListener("DOMContentLoaded", async () => {
    const usernameSelect = document.getElementById("username-select");
    const getRecommendationsButton = document.getElementById("get-recommendations-button");
    const recommendationsContainer = document.getElementById("recommendations-container");

    try {
        const response = await fetch("/api/usernames");
        const data = await response.json();

        if (data.usernames.length === 0) {
            console.warn("No usernames found.");
            return;
        }

        data.usernames.forEach(username => {
            const option = document.createElement("option");
            option.value = username;
            option.textContent = username;
            usernameSelect.appendChild(option);
        });

    } catch (error) {
        console.error("Error fetching usernames:", error);
    }
    // Fetch recommendations when button is clicked
    getRecommendationsButton.addEventListener("click", async () => {
        const selectedUser = usernameSelect.value;
        if (!selectedUser) {
            alert("Please select a user first.");
            return;
        }

        try {
            const response = await fetch(`recommend/${encodeURIComponent(selectedUser)}`);
            const data = await response.json();

            // Clear previous recommendations
            recommendationsContainer.innerHTML = "";

            if (data.error) {
                recommendationsContainer.innerHTML = `<p>${data.error}</p>`;
                return;
            }

            // Display recommendations
            data.recomendaciones.forEach(movie => {
                const movieDiv = document.createElement("div");
                movieDiv.classList.add("movie-card");

                movieDiv.innerHTML = `
                    <h3>${movie.pelicula}</h3>
                    <p class="description">${movie.descripcion}</p>
                `;

                recommendationsContainer.appendChild(movieDiv);
            });
            
        } catch (error) {
            console.error("Error fetching recommendations:", error);
            recommendationsContainer.innerHTML = "<p>Error loading recommendations. Try again later.</p>";
        }
    });
});
