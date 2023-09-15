// let map;
// async function initMap() {
//   const { Map } = await google.maps.importLibrary("maps");

//   map = new Map(document.getElementById("map"), {
//     center: { lat: 12.2323432, lng: 77.73463463 },
//     zoom: 8,
//   });
// }

// function initMap() {
//   var map = new google.maps.Map(document.getElementById('map'), {
//       center: { lat: latitude, lng: longitude },
//       zoom: 15 // Adjust the zoom level as needed
//   });

//   // Create a marker for the specified location
//   var marker = new google.maps.Marker({
//       position: { lat: latitude, lng: longitude },
//       map: map,
//       title: 'Marker Title' // Replace with your marker title
//   });
// }

function initMap() {
  // Initialize the map
  const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: latitude, lng: longitude },
      zoom: 15, // Adjust the zoom level as needed
  });

  // Create a marker at the specified location
  new google.maps.Marker({
      position: { lat: latitude, lng: longitude },
      map: map,
      title: "Location",
  });
}

function convertLocation() {
  const location = document.getElementById("location").value;
  const geocoder = new google.maps.Geocoder();

  geocoder.geocode({ address: location }, (results, status) => {
      if (status === "OK" && results[0]) {
          const latitude = results[0].geometry.location.lat();
          const longitude = results[0].geometry.location.lng();
          
          console.log(latitude);
          console.log(longitude);

          var inputElement = document.getElementById("location");
          var inputValue = inputElement.value;
          if (inputValue === "") 
          {
              alert("Enter a valid location!");
          } 
          else {
              window.open("./maps.html","_self");
          }

      } else {
          alert("Location not found");
      }
  });
}




// function searchLocation() {
//     const locationInput = document.getElementById("location").value;
    
//     // Replace 'YOUR_API_KEY' with your actual Google Maps API key
//     const apiKey = 'AIzaSyAqvqHN7c-tdKqeDUq-0SXOlDpIwZ7lH6A';
    
//     // Construct the Google Maps URL
//     const mapsUrl = `https://www.google.com/maps?q=${locationInput}&key=${apiKey}`;

//     // Open the Google Maps URL in a new window
//     window.open(mapsUrl, '_blank');
// }