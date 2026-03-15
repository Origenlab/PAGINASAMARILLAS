




document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.getElementById('menuToggle');
  const navMenu = document.getElementById('navMenu');

  if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', function() {
      const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';

      
      menuToggle.setAttribute('aria-expanded', !isExpanded);

      
      navMenu.classList.toggle('active');

      
      document.body.style.overflow = isExpanded ? '' : 'hidden';
    });

    
    document.addEventListener('click', function(event) {
      const isClickInside = menuToggle.contains(event.target) || navMenu.contains(event.target);

      if (!isClickInside && navMenu.classList.contains('active')) {
        menuToggle.setAttribute('aria-expanded', 'false');
        navMenu.classList.remove('active');
        document.body.style.overflow = '';
      }
    });

    
    document.addEventListener('keydown', function(event) {
      if (event.key === 'Escape' && navMenu.classList.contains('active')) {
        menuToggle.setAttribute('aria-expanded', 'false');
        navMenu.classList.remove('active');
        document.body.style.overflow = '';
      }
    });

    
    const navLinks = navMenu.querySelectorAll('a');
    navLinks.forEach(link => {
      link.addEventListener('click', function() {
        if (navMenu.classList.contains('active')) {
          menuToggle.setAttribute('aria-expanded', 'false');
          navMenu.classList.remove('active');
          document.body.style.overflow = '';
        }
      });
    });
  }
});




document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const href = this.getAttribute('href');

    
    if (href === '#' || href === '#login' || href === '#registrar') {
      return;
    }

    e.preventDefault();
    const target = document.querySelector(href);

    if (target) {
      const headerOffset = 80;
      const elementPosition = target.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

      window.scrollTo({
        top: offsetPosition
      });
    }
  });
});




window.addEventListener('scroll', function() {
  const header = document.getElementById('header');

  if (window.scrollY > 10) {
    header.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)';
  } else {
    header.style.boxShadow = '0 1px 3px 0 rgba(0, 0, 0, 0.1)';
  }
});




const searchForm = document.querySelector('.search-form');

if (searchForm) {
  searchForm.addEventListener('submit', function(e) {
    const searchInput = this.querySelector('input[name="q"]');

    if (searchInput && searchInput.value.trim() === '') {
      e.preventDefault();
      searchInput.focus();

      
      searchInput.style.borderColor = '#E74C3C';
      setTimeout(() => {
        searchInput.style.borderColor = '';
      }, 2000);
    }
  });
}

console.log(' PaginasAmarillas.mx loaded successfully');
