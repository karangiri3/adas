function planTrip() {

    const destination =
        document.getElementById("destination").value;

    const budget =
        document.getElementById("budget").value;

    const duration =
        document.getElementById("duration").value;

    const travelStyle =
        document.getElementById("style").value;


    if (!destination || !budget || !duration) {

        alert("Please enter destination, budget and duration.");

        return;
    }


    const result =
        document.getElementById("result-content");


    result.innerHTML = `
        <h3>🌍 ${destination} Trip</h3>

        <p>💰 Budget: ₹${budget}</p>

        <p>🗓️ Duration: ${duration}</p>

        <p>🎒 Travel Style: ${travelStyle || "Flexible"}</p>

        <br>

        <p>
            🤖 AI is preparing your personalized itinerary...
        </p>
    `;


    document
        .getElementById("result")
        .scrollIntoView({
            behavior: "smooth"
        });
}