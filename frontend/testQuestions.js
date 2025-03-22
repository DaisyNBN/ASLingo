const answerButton = document.getElementById('answer-btn');
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const questionText = document.getElementById('question-text');

// Hardcoded for now: current question target
const expectedAnswer = "A";

answerButton.addEventListener('click', () => {
  // Step 1: Open the camera
  navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } })
    .then(stream => {
      video.style.display = 'block';
      video.srcObject = stream;
      answerButton.textContent = "Capture";
      // Switch to capture mode on next click
      answerButton.onclick = captureAndSend;
    })
    .catch(err => {
      alert('Error accessing camera: ' + err);
    });
});


