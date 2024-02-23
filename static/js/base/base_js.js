document.addEventListener('DOMContentLoaded', (event) => {
  // Onscroll fixed top navigation
  window.addEventListener('scroll', function() {
    const navigation = document.querySelector('.navigation');
    if (window.scrollY >= 60) {
      navigation.classList.add('sticky-navigation', 'shadow');
    } else {
      navigation.classList.remove('sticky-navigation', 'shadow');
    }
  });

  // Dark theme toggle
  const darkThemeBtn = document.querySelector('.darkthemebtn');
  darkThemeBtn.addEventListener('click', function() {
    document.body.classList.toggle('dark-theme');
  });

  // Back to top button
  const backToTopBtn = document.querySelector('.back-to-top');
  window.addEventListener('scroll', function() {
    if (window.scrollY >= 60) {
      backToTopBtn.classList.add('d-block');
    } else {
      backToTopBtn.classList.remove('d-block');
    }
  });
  backToTopBtn.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
});
