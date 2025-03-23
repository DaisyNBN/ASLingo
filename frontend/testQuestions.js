const questionText = document.getElementById('question-text');
const answerButton = document.getElementById('answer-btn');
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');

console.log("✅ testQuestions.js loaded");

// All 29 ASL characters
const aslCharacters = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
  'U', 'V', 'W', 'X', 'Y', 'Z', 'del', 'nothing', 'space'
];

let expectedAnswer = getRandomCharacter();
let streamStarted = false;

updateQuestionText();

answerButton.addEventListener('click', () => {
  if (!streamStarted) {
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

          // Show correct answer regardless of prediction
          alert(`You signed '${prediction}'. The correct answer was '${expectedAnswer}'.`);

          // Move to next random question
          expectedAnswer = getRandomCharacter();
          updateQuestionText();
          answerButton.textContent = "Capture";
        })
        .catch(err => {
          console.error("API Error:", err);
          alert("Error sending image to backend.");
        });
    }, "image/png");
  }
});

function getRandomCharacter() {
  const randomIndex = Math.floor(Math.random() * aslCharacters.length);
  return aslCharacters[randomIndex];
}

function updateQuestionText() {
  questionText.textContent = `What is “${expectedAnswer}”?`;
}
