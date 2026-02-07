const recordBtn = document.querySelector('.record-btn');
const submitTextBtn = document.querySelector('.submit-text-btn')

let recorder = null;
let stream = null;

recordBtn.addEventListener('click', async function(e) {
    e.preventDefault();
    // If already recording, stop it
    if (recorder && recorder.state === 'recording') {
        recorder.stop();
        console.log('Recording stopped');
        return;
    }

    // Start new recording
    stream = await navigator.mediaDevices.getUserMedia({audio: true});
    recorder = new MediaRecorder(stream);
    const chunks = []; 
    recordBtn.classList.add('recording')

    console.log('Recording start');
    
    recorder.ondataavailable = (e) => chunks.push(e.data);
    
    recorder.onstop = async () => {
        recordBtn.classList.remove('recording')
        const img = recordBtn.querySelector('.mic-img')
        img.src = '/static/spin-circle.gif'
        const blob = new Blob(chunks, {type: 'audio/webm'});
        try {
            const response = await fetch('/record', {
                method: "POST",
                body: blob
            });
            // Reload the page to show the new recording
            window.location.reload();
        } catch (error) {
            alert('Some error has occurred');
        }
        // Stop all tracks to release the microphone
        stream.getTracks().forEach(track => track.stop());
    };
    const img = recordBtn.querySelector('.mic-img')
    img.src = '/static/mic.png'

    recorder.start();
    console.log('Recording started...');

    // Auto-stop after 30 seconds
    setTimeout(() => {
        if (recorder && recorder.state === 'recording') {
            recorder.stop();
            console.log('Recording auto-stopped after 30 seconds');
        }
    }, 30000);
})

submitTextBtn.addEventListener('click', async function (e) {
    const inputText = document.getElementById('input-text').value
    if (inputText) {
        try {
            const response = await fetch ('/submit-text', {
                method: 'POST', 
                body: inputText
            })
            window.location.reload();
        } catch (error) {
            alert('some error occur')
        }
    }
})