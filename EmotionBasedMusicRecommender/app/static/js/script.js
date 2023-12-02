function displaySpotifyTrack() {
    var emotionInput = document.getElementById('emotion-input');
    var spotifyIframeDiv = document.getElementById('spotify-iframe');
    var recmessage = document.getElementById('recommendation-message');

    if (emotionInput.value.trim() === '') {
        // Empty check
        emotionInput.classList.add('empty-input'); 
        emotionInput.style.borderColor = 'red';
        emotionInput.placeholder = 'This field cannot be empty. Tell us about your day :)';
        recmessage.style.display = 'none';
        spotifyIframeDiv.style.display = 'none';
        return; 
    } else {
        emotionInput.classList.remove('empty-input'); 
    }

    var recommendationMessage = document.getElementById('recommendation-message');
    recommendationMessage.style.display = 'block';
    recommendationMessage.style.opacity = 1;

    var iframeHtml = '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/3USxtqRwSYz57Ewm6wWRMp?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>';
    spotifyIframeDiv.innerHTML = iframeHtml;
    spotifyIframeDiv.style.display = 'block';
    spotifyIframeDiv.style.opacity = 1;
}


document.getElementById('emotion-input').addEventListener('focus', function() {
    this.classList.remove('empty-input'); 
    this.style.borderColor = ''; 
    this.placeholder = 'How are you feeling today?'; 
});
