const { exec } = require('child_process');

const answerButton = document.getElementById('answer-btn');

answerButton.addEventListener('click', () => {
  // Launch Python backend (adjust path as needed)
  exec('conda run -n asl-env python ../asl-classifier/app.py', (err, stdout, stderr) => {
    if (err) {
      console.error('Failed to launch Python app:', err);
    } else {
      console.log('Python app launched!');
    }
  });
});
