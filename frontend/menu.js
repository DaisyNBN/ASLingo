const { exec } = require('child_process');

document.getElementById('practice-btn').addEventListener('click', () => {
    console.log("Practice button clicked!");
    fetch("http://localhost:5000/")
});
