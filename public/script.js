document.getElementById('downloadButton').addEventListener('click', function() {
    var url = document.getElementById('urlInput').value;

    // Send the URL to your server for download
    fetch(`/download?url=${url}`, { method: 'GET' })
        .then(response => response.text())
        .then(data => {
            alert(data); // Show a message to the user
        })
        .catch(error => console.error('Error:', error));
});
