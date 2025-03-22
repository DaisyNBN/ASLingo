const video = document.getElementById('video');
const captureButton = document.getElementById('capture-btn');
const canvas = document.getElementById('canvas');

// Automatically start camera when page loads
navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => {
    alert('Error accessing camera: ' + err);
  });

captureButton.addEventListener('click', () => {
  const context = canvas.getContext('2d');
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  const imageData = canvas.toDataURL('image/png');
  console.log('Captured Image:', imageData);
  alert('Image captured! Ready to send to backend.');
});
