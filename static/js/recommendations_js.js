document.addEventListener("DOMContentLoaded", async () => {
    const usernameSelect = document.getElementById("username-select");

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
});
