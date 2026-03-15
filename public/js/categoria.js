

document.addEventListener('DOMContentLoaded', function() {

  
  
  
  const filterToggles = document.querySelectorAll('.filter-toggle');

  filterToggles.forEach(toggle => {
    toggle.addEventListener('click', function() {
      const isExpanded = this.getAttribute('aria-expanded') === 'true';
      const filterContent = this.nextElementSibling;

      
      this.setAttribute('aria-expanded', !isExpanded);

      
      if (filterContent) {
        if (isExpanded) {
          filterContent.style.display = 'none';
        } else {
          filterContent.style.display = 'block';
        }
      }
    });
  });

  
  
  
  const clearFiltersBtn = document.querySelector('.btn-clear-filters');

  if (clearFiltersBtn) {
    clearFiltersBtn.addEventListener('click', function() {
      
      const checkboxes = document.querySelectorAll('.filter-checkbox input[type="checkbox"], .filter-radio input[type="radio"], .filter-switch input[type="checkbox"]');
      checkboxes.forEach(checkbox => {
        checkbox.checked = false;
      });

      
      const searchInputs = document.querySelectorAll('.filter-search-input');
      searchInputs.forEach(input => {
        input.value = '';
      });

      
      console.log('Filters cleared');
    });
  }

  
  
  
  const filterSearchInputs = document.querySelectorAll('.filter-search-input');

  filterSearchInputs.forEach(input => {
    input.addEventListener('input', function() {
      const searchTerm = this.value.toLowerCase();
      const filterContent = this.closest('.filter-content');
      const checkboxes = filterContent.querySelectorAll('.filter-checkbox');

      checkboxes.forEach(checkbox => {
        const label = checkbox.querySelector('span').textContent.toLowerCase();
        if (label.includes(searchTerm)) {
          checkbox.style.display = 'flex';
        } else {
          checkbox.style.display = 'none';
        }
      });
    });
  });

  
  
  
  const showMoreButtons = document.querySelectorAll('.btn-show-more');

  showMoreButtons.forEach(button => {
    button.addEventListener('click', function() {
      
      console.log('Show more clicked');
      this.textContent = 'Ver menos ubicaciones';
    });
  });

  
  
  
  const allFilters = document.querySelectorAll('.filter-checkbox input, .filter-radio input, .filter-switch input');

  allFilters.forEach(filter => {
    filter.addEventListener('change', function() {
      
      const activeFilters = {
        locations: [],
        services: [],
        certifications: [],
        rating: null,
        availability24h: false
      };

      
      document.querySelectorAll('.filter-checkbox input[name="location"]:checked').forEach(cb => {
        activeFilters.locations.push(cb.value);
      });

      
      document.querySelectorAll('.filter-checkbox input[name="service"]:checked').forEach(cb => {
        activeFilters.services.push(cb.value);
      });

      
      document.querySelectorAll('.filter-checkbox input[name="cert"]:checked').forEach(cb => {
        activeFilters.certifications.push(cb.value);
      });

      
      const ratingChecked = document.querySelector('.filter-radio input[name="rating"]:checked');
      if (ratingChecked) {
        activeFilters.rating = ratingChecked.value;
      }

      
      const availability24h = document.querySelector('.filter-switch input[name="24h"]');
      if (availability24h && availability24h.checked) {
        activeFilters.availability24h = true;
      }

      console.log('Active filters:', activeFilters);

      
      
    });
  });

  
  
  
  const sortSelect = document.getElementById('sort');

  if (sortSelect) {
    sortSelect.addEventListener('change', function() {
      const sortValue = this.value;
      console.log('Sort by:', sortValue);

      
      
    });
  }

  
  
  
  
  const filtersSidebar = document.querySelector('.filters-sidebar');

  if (window.innerWidth < 1024 && filtersSidebar) {
    
    const toggleFiltersBtn = document.createElement('button');
    toggleFiltersBtn.className = 'btn btn-primary mobile-filters-toggle';
    toggleFiltersBtn.innerHTML = `
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <line x1="4" y1="21" x2="4" y2="14"/>
        <line x1="4" y1="10" x2="4" y2="3"/>
        <line x1="12" y1="21" x2="12" y2="12"/>
        <line x1="12" y1="8" x2="12" y2="3"/>
        <line x1="20" y1="21" x2="20" y2="16"/>
        <line x1="20" y1="12" x2="20" y2="3"/>
        <line x1="1" y1="14" x2="7" y2="14"/>
        <line x1="9" y1="8" x2="15" y2="8"/>
        <line x1="17" y1="16" x2="23" y2="16"/>
      </svg>
      Filtros
    `;

    toggleFiltersBtn.style.cssText = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      z-index: 999;
      box-shadow: var(--shadow-xl);
      display: none;
    `;

    
    if (window.innerWidth < 1024) {
      toggleFiltersBtn.style.display = 'flex';
    }

    
    toggleFiltersBtn.addEventListener('click', function() {
      filtersSidebar.style.position = 'fixed';
      filtersSidebar.style.top = '80px';
      filtersSidebar.style.left = '0';
      filtersSidebar.style.right = '0';
      filtersSidebar.style.bottom = '0';
      filtersSidebar.style.zIndex = '1000';
      filtersSidebar.style.maxHeight = 'calc(100vh - 80px)';
      filtersSidebar.style.overflowY = 'auto';
      filtersSidebar.style.display = filtersSidebar.style.display === 'none' ? 'block' : 'none';
    });

    document.body.appendChild(toggleFiltersBtn);
  }

  
  
  
  const faqQuestions = document.querySelectorAll('.faq-question');

  faqQuestions.forEach(question => {
    question.addEventListener('click', function() {
      const faqId = this.getAttribute('data-faq');
      const answer = document.getElementById(`faq-${faqId}`);
      const isExpanded = this.getAttribute('aria-expanded') === 'true';

      
      faqQuestions.forEach(q => {
        if (q !== this) {
          q.setAttribute('aria-expanded', 'false');
          const otherId = q.getAttribute('data-faq');
          const otherAnswer = document.getElementById(`faq-${otherId}`);
          if (otherAnswer) {
            otherAnswer.classList.remove('active');
          }
        }
      });

      
      this.setAttribute('aria-expanded', !isExpanded);
      if (answer) {
        if (isExpanded) {
          answer.classList.remove('active');
        } else {
          answer.classList.add('active');
        }
      }
    });
  });

});






function updateResults(filters) {
  console.log('Updating results with filters:', filters);

  
  
  
  
  
  
  
  
  
}


function updateBusinessListings(businesses) {
  const listingsContainer = document.querySelector('.business-listings');
  if (!listingsContainer) return;

  
  console.log('Updating listings with', businesses.length, 'businesses');
}


function updateResultsCount(total) {
  const countElement = document.querySelector('.results-info h2');
  if (countElement) {
    countElement.textContent = `${total} empresas de Seguridad Privada`;
  }
}

console.log('✅ Categoria.js loaded successfully');
