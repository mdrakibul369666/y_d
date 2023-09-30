const express = require('express');
const app = express();
const port = process.env.PORT || "3000";
const { exec } = require('child_process');

app.use(express.static('public')); // Serve static files from the 'public' directory

app.get('/download', (req, res) => {
  const url = req.query.url; // Get the YouTube video URL from query parameters

  exec(`python download_video.py ${url}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      res.status(500).send('Error occurred while downloading the video');
    } else {
      const fileName = 'downloaded_video.mp4'; // Assuming the downloaded file is in mp4 format
      res.download(fileName); // Send the file to the user's browser
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
