// app.js
const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Setting up static directory
app.use('/static', express.static(path.join(__dirname, 'static')));


// Route to return HTML file
app.get('/', (req, res) => {
  // Path to HTML file
  const filePath = path.join(__dirname, '.', 'index.html');

  // Sending the file as response
  res.sendFile(filePath);
});

// Starting the server
app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
