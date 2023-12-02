function displaySpotifyTrack() {
    var recommendationMessage = document.getElementById('recommendation-message');
    recommendationMessage.style.display = 'block';
    recommendationMessage.style.opacity = 1;

    var iframeHtml = '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/3USxtqRwSYz57Ewm6wWRMp?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>';
    var spotifyIframeDiv = document.getElementById('spotify-iframe');
    spotifyIframeDiv.innerHTML = iframeHtml;
    spotifyIframeDiv.style.display = 'block';
    spotifyIframeDiv.style.opacity = 1;
}
