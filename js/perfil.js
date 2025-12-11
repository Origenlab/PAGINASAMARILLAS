

document.addEventListener('DOMContentLoaded', function() {

  
  
  
  const galleryThumbs = document.querySelectorAll('.gallery-thumb');
  const mainImage = document.querySelector('.business-main-image img');

  if (galleryThumbs.length > 0 && mainImage) {
    galleryThumbs.forEach(thumb => {
      thumb.addEventListener('click', function() {
        
        galleryThumbs.forEach(t => t.classList.remove('active'));

        
        this.classList.add('active');

        
        const thumbImg = this.querySelector('img');
        if (thumbImg) {
          
          mainImage.src = thumbImg.src.replace('120x80', '600x400');
          mainImage.alt = thumbImg.alt;
        }
      });
    });
  }

  
  
  
  const btnContactForm = document.getElementById('btn-contact-form');
  const contactFormWrapper = document.querySelector('.contact-form-wrapper');

  if (btnContactForm && contactFormWrapper) {
    btnContactForm.addEventListener('click', function() {
      
      contactFormWrapper.scrollIntoView({
        block: 'start'
      });

      
      const firstInput = contactFormWrapper.querySelector('input');
      if (firstInput) {
        firstInput.focus();
      }
    });
  }

  
  
  
  const contactForm = document.getElementById('contact-form');

  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();

      
      const formData = new FormData(contactForm);
      const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        phone: formData.get('phone'),
        company: formData.get('company'),
        service: formData.get('service'),
        message: formData.get('message'),
        business: 'origins-private-security', 
        timestamp: new Date().toISOString()
      };

      
      console.log('Form submitted:', data);

      
      showFormSuccess();

      
      contactForm.reset();

      
      
      
      
      
      
      
      
      
      
      
      
      
      
    });
  }

  
  
  
  function showFormSuccess() {
    const formWrapper = document.querySelector('.contact-form-wrapper');

    
    const successMsg = document.createElement('div');
    successMsg.className = 'form-message success';
    successMsg.innerHTML = `
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
        <polyline points="22 4 12 14.01 9 11.01"/>
      </svg>
      <div>
        <strong>¡Mensaje enviado con éxito!</strong>
        <p>Nos pondremos en contacto contigo en las próximas 24 horas.</p>
      </div>
    `;

    
    successMsg.style.cssText = `
      display: flex;
      gap: 12px;
      padding: 16px;
      background-color: #D1FAE5;
      border: 1px solid #10B981;
      border-radius: 8px;
      margin-bottom: 16px;
    `;

    successMsg.querySelector('svg').style.cssText = `
      color: #10B981;
      flex-shrink: 0;
    `;

    
    formWrapper.insertBefore(successMsg, contactForm);

    
    setTimeout(() => {
      successMsg.remove();
    }, 5000);
  }

  function showFormError() {
    const formWrapper = document.querySelector('.contact-form-wrapper');

    
    const errorMsg = document.createElement('div');
    errorMsg.className = 'form-message error';
    errorMsg.innerHTML = `
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"/>
        <line x1="12" y1="8" x2="12" y2="12"/>
        <line x1="12" y1="16" x2="12.01" y2="16"/>
      </svg>
      <div>
        <strong>Error al enviar mensaje</strong>
        <p>Por favor intenta de nuevo o llámanos directamente.</p>
      </div>
    `;

    
    errorMsg.style.cssText = `
      display: flex;
      gap: 12px;
      padding: 16px;
      background-color: #FEE2E2;
      border: 1px solid #EF4444;
      border-radius: 8px;
      margin-bottom: 16px;
    `;

    errorMsg.querySelector('svg').style.cssText = `
      color: #EF4444;
      flex-shrink: 0;
    `;

    
    formWrapper.insertBefore(errorMsg, contactForm);

    
    setTimeout(() => {
      errorMsg.remove();
    }, 5000);
  }

  
  
  
  const phoneInput = document.getElementById('phone');

  if (phoneInput) {
    phoneInput.addEventListener('input', function(e) {
      
      let value = e.target.value.replace(/\D/g, '');

      
      if (value.length > 10) {
        value = value.substring(0, 10);
      }

      
      if (value.length >= 2) {
        value = value.substring(0, 2) + ' ' + value.substring(2);
      }
      if (value.length >= 7) {
        value = value.substring(0, 7) + ' ' + value.substring(7);
      }

      e.target.value = value;
    });
  }

  
  
  
  const ratingLink = document.querySelector('.rating-link');

  if (ratingLink) {
    ratingLink.addEventListener('click', function(e) {
      e.preventDefault();
      const reviewsSection = document.getElementById('reviews');
      if (reviewsSection) {
        reviewsSection.scrollIntoView({
          block: 'start'
        });
      }
    });
  }

  
  
  
  if ('IntersectionObserver' in window) {
    const images = document.querySelectorAll('img[data-src]');

    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          observer.unobserve(img);
        }
      });
    });

    images.forEach(img => imageObserver.observe(img));
  }

  
  
  

  
  const phoneLinks = document.querySelectorAll('a[href^="tel:"]');
  phoneLinks.forEach(link => {
    link.addEventListener('click', function() {
      console.log('Phone click tracked:', this.href);
      
      
      
      
      
    });
  });

  
  const whatsappLinks = document.querySelectorAll('a[href*="wa.me"]');
  whatsappLinks.forEach(link => {
    link.addEventListener('click', function() {
      console.log('WhatsApp click tracked:', this.href);
      
      
      
      
    });
  });

  
  const emailLinks = document.querySelectorAll('a[href^="mailto:"]');
  emailLinks.forEach(link => {
    link.addEventListener('click', function() {
      console.log('Email click tracked:', this.href);
      
    });
  });

  
  
  
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






function isValidEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}


function isValidPhone(phone) {
  const digits = phone.replace(/\D/g, '');
  return digits.length === 10;
}

console.log('✅ Perfil.js loaded successfully');
