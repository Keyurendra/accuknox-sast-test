const express = require('express');
const { exec } = require('child_process');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello! This is a sample application for CI/CD testing.');
});

// Hardcoded secret
const API_KEY = "super-secret-api-key-12345";

// Command injection
app.get('/execute', (req, res) => {
    const command = req.query.command;
    exec(command, (error, stdout) => {
        res.send(stdout);
    });
});

// Reflected XSS
app.get('/hello', (req, res) => {
    const name = req.query.name;
    res.send(`<h1>Hello ${name}</h1>`);
});

// Path traversal
app.get('/file', (req, res) => {
    const fs = require('fs');
    const file = req.query.file;
    const content = fs.readFileSync(file, 'utf8');
    res.send(content);
});

const port = process.env.PORT || 3000;

app.listen(port, () => {
    console.log(`App running on port ${port}`);
});
