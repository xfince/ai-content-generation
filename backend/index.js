// backend/index.js
require('dotenv').config(); // Add this line at the top of your file

const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Access the API key from environment variables
const apiKey = process.env.GEMINI_API_KEY;

// Endpoint for generating content
app.post('/generate', async (req, res) => {
  const { prompt } = req.body;
  try {
    // Pass the API key in the request to the Python service
    const response = await axios.post('http://localhost:5000/generate', { prompt, apiKey });
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Content generation failed' });
  }
});

// Endpoint for moderating content
app.post('/moderate', async (req, res) => {
  const { content } = req.body;
  try {
    // Pass the API key in the request to the Python service
    const response = await axios.post('http://localhost:5000/moderate', { content, apiKey });
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Content moderation failed' });
  }
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
