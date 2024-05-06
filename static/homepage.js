document.addEventListener('DOMContentLoaded', function() {
    const trailCount = 6; // Number of trail elements
    const delay = 115; // Delay in milliseconds between elements fading
    let notes = [];

    for (let i = 0; i < trailCount; i++) {
        let note = document.createElement('i');
        note.className = 'fas fa-music note';
        document.body.appendChild(note);
        notes.push(note);
    }

    document.addEventListener('mousemove', function(event) {
        notes.forEach((note, index) => {
            setTimeout(() => {
                note.style.left = event.pageX + 'px';
                note.style.top = event.pageY + 'px';
                note.style.opacity = 1; // Make the note visible

                
            }, index * delay);
        });
    });
});



// Define only the image filenames in the array
var albums = [
    'MariachiVargas.jpg',
    'SonMadera.jpg',
    'LosTigres.png',
    'LosReyes.jpg'
];
var currentAlbumIndex = 0;

var basePath = '/static/Images/';  // Adjust if your static path is different

function changeAlbum(direction) {
    // This check allows the function to be used with automatic and manual triggers
    if (direction !== undefined) {
        currentAlbumIndex += direction;
    } else {
        currentAlbumIndex++; // This will just increment the index for automatic changes
    }

    // Wrapping around the index if it goes out of the bounds of the array
    if (currentAlbumIndex >= albums.length) {
        currentAlbumIndex = 0;
    } else if (currentAlbumIndex < 0) {
        currentAlbumIndex = albums.length - 1;
    }

    // Update the source of the album cover image
    document.getElementById('albumImage').src = basePath + albums[currentAlbumIndex];
}

// Set up an interval to change the album cover every 3 seconds
setInterval(function() {
    changeAlbum();  // Calling without arguments for automatic change
}, 4000);  // 3000 milliseconds = 3 seconds

function changeAlbum(direction) {
    var coverImage = document.getElementById('albumImage');
    var albumCover = coverImage.parentNode;

    // Fade out the image
    albumCover.classList.add('fade-out');

    // Wait for fade out to finish before changing the image and fading back in
    setTimeout(function() {
        if (direction !== undefined) {
            currentAlbumIndex += direction;
        } else {
            currentAlbumIndex++; // This will just increment the index for automatic changes
        }

        if (currentAlbumIndex >= albums.length) {
            currentAlbumIndex = 0;
        } else if (currentAlbumIndex < 0) {
            currentAlbumIndex = albums.length - 1;
        }

        coverImage.src = basePath + albums[currentAlbumIndex];

        // Wait for the new image to load before fading it back in
        coverImage.onload = function() {
            albumCover.classList.remove('fade-out');
        };
    }, 400);  // Match the timeout to the CSS opacity transition duration
}


