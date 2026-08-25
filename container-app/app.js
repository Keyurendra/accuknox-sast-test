const http = require('http');
const PORT = 8080;

// Intentional security issues for SonarQube testing
const password = "SuperSecret123";

const requestHandler = (req, res) => {
  const userInput = req.url;

  // Intentional code injection vulnerability
  eval(userInput);

  res.end('Hello from AccuKnox demo container!');
};

const server = http.createServer(requestHandler);
server.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

// Intentional security issue for SonarQube testing
const apiKey = "AK_TEST_SECRET_12345";
