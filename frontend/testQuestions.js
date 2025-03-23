const questionText = document.getElementById('question-text');
const answerButton = document.getElementById('answer-btn');
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');

// Set the expected answer here (could be dynamic later)
const expectedAnswer = "A";

let streamStarted = false;

// Update question text
questionText.textContent = `Question 1: What is “${expectedAnswer}”?`;

answerButton.addEventListener('click', () => {
  if (!streamStarted) {
    // Start webcam
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } })
      .then(stream => {
        video.srcObject = stream;
        video.style.display = 'block';
        canvas.style.display = 'none';
        streamStarted = true;
        answerButton.textContent = "Capture";
      })
      .catch(err => {
        alert("Camera access failed: " + err);
      });
  } else {
    // Capture frame and send to backend
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob((blob) => {
      const formData = new FormData();
      formData.append("file", blob, "capture.png");

      fetch("http://127.0.0.1:8000/predict/", {
        method: "POST",
        body: formData
      })
        .then(res => res.json())
        .then(data => {
          const prediction = data.prediction;
          if (prediction === expectedAnswer) {
            alert(`✅ Correct! You signed '${prediction}'`);
          } else {
            alert(`❌ Incorrect. You signed '${prediction}', but the correct answer was '${expectedAnswer}'`);
          }
        })
        .catch(err => {
          console.error("API Error:", err);
          alert("Error sending image to backend.");
        });
    }, "image/png");
  }
});
