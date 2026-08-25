const http = require('http');
const PORT = 8080;

// Intentional security issues for SonarQube testing
const password = "SuperSecret123";

const requestHandler = (req, res) => {
  const userInput = req.url;

  // Intentional code injection vulnerability
  eval(userInput);

  // Intentional command injection vulnerability
  const { exec } = require('child_process');
  exec("ping -c 1 " + userInput);

  // Intentional weak cryptographic algorithm
  const crypto = require('crypto');
  const hash = crypto.createHash('md5').update(userInput).digest('hex');

  // Intentional insecure HTTP request
  const httpRequest = require('http');
  httpRequest.get("http://example.com/api?token=SuperSecretToken123");

  res.end('Hello from AccuKnox demo container!');
};

const server = http.createServer(requestHandler);
server.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

// Intentional security issue for SonarQube testing
const apiKey = "AK_TEST_SECRET_12345";
