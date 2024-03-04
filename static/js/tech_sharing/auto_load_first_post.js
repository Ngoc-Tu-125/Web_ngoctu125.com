document.addEventListener('DOMContentLoaded', function() {
    // Try to find the first tech-sharing title link
    var firstPostLink = document.querySelector('.tech-sharing-title-link');

    // If the link exists, simulate a click on it
    if (firstPostLink) {
        firstPostLink.click();
    }
});