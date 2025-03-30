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
    const submitButton = document.getElementById("submit-button");

    if (submitButton) {
        submitButton.addEventListener("click", () => {
            const username = document.getElementById("username").value.trim();

            if (!username) {
                alert("Por favor, ingresa tu nombre de usuario antes de enviar las valoraciones.");
                return; // Detiene la ejecución si el campo está vacío
            }

            const ratingElements = document.querySelectorAll(".rating");

            const ratings = Array.from(ratingElements).map(select => 
                select.value ? parseInt(select.value) : 0
            );

            console.log(`Usuario: ${username}`);
            console.log("Valoraciones de las películas:", ratings);
        });
    } else {
        console.error("No se encontró el botón de enviar.");
    }
});



/*
document.getElementById("submit-button").addEventListener("click", async () => {
    const ratingElements = document.querySelectorAll(".rating");
    const ratings = Array.from(ratingElements).map(select => select.value);

    const response = await fetch("/api/rate_movies", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ ratings })
    });

    if (response.ok) {
        alert("Calificaciones enviadas correctamente.");
    } else {
        alert("Error al enviar las calificaciones.");
    }
});
*/
