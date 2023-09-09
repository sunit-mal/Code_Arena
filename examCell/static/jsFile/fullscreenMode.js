document.getElementById('fullscreenBtn').addEventListener('click', () => {
        enterFullscreen();
        showQuestion();

})
document.getElementById('Start').addEventListener('click', () => {
        startCamera();
})



function requestFullscreen() {
    var elem = document.documentElement; // Get the root element of the document

    // Check if fullscreen is supported by the browser
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.mozRequestFullScreen) { /* Firefox */
        elem.mozRequestFullScreen();
    } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE/Edge */
        elem.msRequestFullscreen();
    }

    // Add event listener to detect fullscreen change
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    document.addEventListener('webkitfullscreenchange', handleFullscreenChange);
    document.addEventListener('mozfullscreenchange', handleFullscreenChange);
    document.addEventListener('MSFullscreenChange', handleFullscreenChange);

}

// Function to enter fullscreen when the button is clicked
function enterFullscreen() {
    requestFullscreen();
}

// Function to handle fullscreen change event
function handleFullscreenChange() {
    if (!document.fullscreenElement && !document.mozFullScreenElement && !document.webkitFullscreenElement && !document.msFullscreenElement) {
        // User exited fullscreen mode
        alert("You are trying to cheat, so I will automatically submit your answer sheet.");
        document.getElementById('btn').click();
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

        // Set the stream as the source for the video element
        videoElement.srcObject = stream;
        document.getElementById('fullscreenBtn').style.display = 'block';
        document.getElementById('Start').style.display = 'none';

    } 
    catch (error) {
        alert("Please access your camera "+error);
    }
}

    // Call the startCamera function when the page loads
    // window.onload = startCamera;