let frameInterval;
let alertCount = 0;

document.getElementById('fullscreenBtn').addEventListener('click', () => {
    enterFullscreen();
    showQuestion();

})
document.getElementById('Start').addEventListener('click', () => {
    startCamera();
})



function requestFullscreen() {
    const navbar = document.getElementById('nav');
    document.body.removeChild(navbar);
    var elem = document.documentElement;

    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.mozRequestFullScreen) { /* Firefox */
        elem.mozRequestFullScreen();
    } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE/Edge */
        elem.msRequestFullscreen();
    }

    document.addEventListener('fullscreenchange', handleFullscreenChange);
    document.addEventListener('webkitfullscreenchange', handleFullscreenChange);
    document.addEventListener('mozfullscreenchange', handleFullscreenChange);
    document.addEventListener('MSFullscreenChange', handleFullscreenChange);

}

function enterFullscreen() {
    requestFullscreen();
    frameInterval = setInterval(sendFrame, 1000); // Start sending frames when entering fullscreen
}

// Function to handle fullscreen change event
function handleFullscreenChange() {
    if (!document.fullscreenElement && !document.mozFullScreenElement && !document.webkitFullscreenElement && !document.msFullscreenElement) {
        document.getElementById('btn').click();
        alert("You are trying to cheat, so I will automatically submit your answer sheet.");
    }
}

function showQuestion() {
    document.getElementById('questions').style.display = 'block';
    document.getElementById('fullscreenBtn').style.display = 'none';
    document.getElementById('Start').style.display = 'none';
}

const videoElement = document.getElementById('videoElement');

// Function to start the camera stream
async function startCamera() {
    try {
        // Get user media (access camera)
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });

        videoElement.srcObject = stream;
        document.getElementById('fullscreenBtn').style.display = 'block';
        document.getElementById('Start').style.display = 'none';

    }
    catch (error) {
        alert("Please access your camera " + error);
    }
}

async function sendFrame() {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;
    context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

    const imageData = canvas.toDataURL('image/jpeg');

    try {
        const response = await fetch('/recognize-face/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Alert-Count': alertCount,
            },
            body: JSON.stringify({ image: imageData }),
        });

        const result = await response.json();
        if (result.status === 'success') {
            alertCount = result.alertCount
            console.log(alertCount);
        } else {
            showToast(`More than one face detected. you have remaining ${alertCount < 10 ? 10 - alertCount : 0} chances`, 3000);
            alertCount = result.alertCount
            console.log(alertCount);

            if (alertCount >= 12) {
                document.getElementById('btn').click();
                alert("Multiple face detected, so I will automatically submit your answer sheet.");
            }
        }
    } catch (error) {
        console.error('Error sending frame:', error);
    }
}

function showToast(message, duration = 3000) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.classList.add('show');
    toast.innerText = message;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.classList.remove('show');
        toast.classList.add('hide');
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 500);
    }, duration);
}

// Disable right-click menu
document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
}, false);

document.addEventListener('keydown', function (e) {

    if (e.keyCode == 123) {
        e.preventDefault();
    }

    if ((e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74)) || // Ctrl+Shift+I or Ctrl+Shift+J
        (e.ctrlKey && (e.keyCode == 85 || e.keyCode == 83))) { // Ctrl+U or Ctrl+S
        e.preventDefault();
    }
}, false);
