// Keep track of the currently selected link
let currentSelectedLink = null;

// JavaScript function to load post content dynamically and highlight the selected link
function loadPostContent(slug, clickedLink) {
    if (currentSelectedLink) {
        currentSelectedLink.classList.remove('selected');
    }
    currentSelectedLink = clickedLink;
    clickedLink.classList.add('selected');

    fetch(`/tech-sharing/${slug}/`)
        .then(response => response.json())
        .then(data => {
            const contentDiv = document.getElementById('tech-sharing-content');
            contentDiv.innerHTML = data.content;

            // Apply syntax highlighting
            contentDiv.querySelectorAll('pre code').forEach(block => {
                hljs.highlightBlock(block);
            });

            // Automatically add IDs to headers based on the sections data
            data.sections.forEach(section => {
                // Find the header by text. Note: This requires a custom function to handle non-jQuery environments.
                let headers = contentDiv.querySelectorAll(section.tag);
                headers.forEach(header => {
                    if (header.textContent === section.text) {
                        header.id = section.id; // Set the ID for the header
                    }
                });
            });

            // Update the sections list
            const sectionsList = document.getElementById('sections-list');
            sectionsList.innerHTML = ''; // Clear existing sections
            data.sections.forEach(section => {
                const listItem = document.createElement('li');
                listItem.className = 'nav-item';
                if (section.tag === 'h3') {
                    listItem.classList.add('h3-style'); // Add a class for h3 styles
                }

                const anchor = document.createElement('a');
                anchor.href = `#${section.id}`;
                anchor.className = 'tech-sections-menu-link nav-link';
                anchor.textContent = section.text;

                // Smooth scroll to the section on click
                anchor.addEventListener('click', (e) => {
                    e.preventDefault(); // Prevent default anchor behavior
                    const targetElement = document.getElementById(section.id);
                    if (targetElement) {
                        targetElement.scrollIntoView({
                            behavior: 'smooth'
                        });
                    }
                });

                listItem.appendChild(anchor);
                sectionsList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error loading the post content:', error));
}