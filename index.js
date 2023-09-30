const express = require('express');
const app = express();
const port = process.env.PORT || "3000";
const { exec } = require('child_process');
const fs = require('fs');

app.use(express.static('public'));

app.get('/download', (req, res) => {
  const url = req.query.url;

  exec(`python3 download_video.py ${url}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      res.status(500).send('Error occurred while downloading the video');
    } else {
      const fileName = stdout.trim();
      const filePath = `./${fileName}`;

      res.download(filePath, fileName, (err) => {
        if (err) {
          console.error(`Error: ${err.message}`);
          res.status(500).send('Error occurred while sending the file');
        } else {
          // Delete the file after the download is complete
          fs.unlink(filePath, (err) => {
            if (err) {
              console.error(`Error deleting file: ${err.message}`);
            } else {
              console.log(`File ${fileName} deleted successfully`);
            }
          });
        }
      });
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
