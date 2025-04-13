document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map centered on Reno-Tahoe area
    var map = L.map('map').setView([39.5296, -119.8138], 10);

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    // Fetch leg data from Flask API
    fetch('/api/legs')
        .then(response => response.json())
        .then(legs => {
            legs.forEach(leg => {
                // Draw a line for each leg
                var polyline = L.polyline([leg.start_coords, leg.end_coords], {
                    color: 'blue',
                    weight: 3
                }).addTo(map);

                // Popup content
                var popupContent = `
                    <b>Leg ${leg.leg}</b><br>
                    Distance: ${leg.distance} miles<br>
                    Elevation Gain: ${leg.elevation_gain} ft<br>
                    Difficulty: ${leg.difficulty}
                `;

                // Bind popup to polyline with hover
                polyline.bindPopup(popupContent, { autoClose: false });
                polyline.on('mouseover', function(e) {
                    this.openPopup();
                });
                polyline.on('mouseout', function(e) {
                    this.closePopup();
                });
            });

            // Fit map to bounds of all legs
            var bounds = legs.map(leg => [leg.start_coords, leg.end_coords]).flat();
            map.fitBounds(bounds);
        });
});