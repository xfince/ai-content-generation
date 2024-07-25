// backend/index.js
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Endpoint for generating content
app.post('/generate', async (req, res) => {
  const { prompt } = req.body;
  try {
    // Call your Python service to generate content
    const response = await axios.post('http://localhost:5000/generate', { prompt });
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Content generation failed' });
  }
});

// Endpoint for moderating content
app.post('/moderate', async (req, res) => {
  const { content } = req.body;
  try {
    // Call your Python service to moderate content
    const response = await axios.post('http://localhost:5000/moderate', { content });
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Content moderation failed' });
  }
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
