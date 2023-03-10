// Créer une nouvelle carte
var myMap = L.map('map').setView([-18.766947, 46.869107], 10);

// Ajouter une couche de tuiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
  maxZoom: 18,
}).addTo(myMap);

// Ajouter des données géospatiales à la carte
var geojsonFeature = {"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}, "features": []};
L.geoJSON(geojsonFeature).addTo(myMap);
