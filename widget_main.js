(function () {
    // Create the widget container
    var widgetContainer = document.createElement('div');
    widgetContainer.id = 'ai-education-widget';

    // Define the HTML content for the widget
    var widgetHTML = `
        <div id="query-input-area">
            <input type="text" id="user-query" placeholder="Ask me about courses..." />
            <button id="submit-query">Submit</button>
        </div>
        <div id="recommendation-area"></div>
    `;

    widgetContainer.innerHTML = widgetHTML;
    document.body.appendChild(widgetContainer);

    // Function to call the Flask backend API
    async function callBackendAPI(userQuery) {
        try {
            const response = await fetch('', { // Ensure the URL matches your Flask app's route
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userQuery }),
            });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            return data.response; // Adjust this based on how you structure your response in Flask
        } catch (error) {
            console.error('There has been a problem with your fetch operation:', error);
            return "Sorry, there was an error processing your request. Please try again.";
        }
    }

    // Event listener for the submit button
    document.getElementById('submit-query').addEventListener('click', function () {
        var userQuery = document.getElementById('user-query').value;
        document.getElementById('recommendation-area').innerText = "Searching for: " + userQuery + "...";

        // Call your backend API and display the recommendations
        callBackendAPI(userQuery).then(response => {
            document.getElementById('recommendation-area').innerText = response;
        });
    });
})();
