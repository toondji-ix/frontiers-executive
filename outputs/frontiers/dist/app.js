const menu = document.querySelector('.menu');
const navigation = document.querySelector('#navigation');
menu.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(open));
  menu.textContent = open ? 'Close' : 'Menu';
  navigation.classList.toggle('open', open);
});
navigation.addEventListener('click', event => {
  if (!event.target.closest('a')) return;
  navigation.querySelectorAll('a').forEach(a => a.classList.toggle('active', a === event.target));
  navigation.classList.remove('open');
  menu.setAttribute('aria-expanded', 'false');
  menu.textContent = 'Menu';
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
    menu.click();
    menu.focus();
  }
});

const enquiryForm = document.querySelector('#enquiry-form');
if (enquiryForm) {
  const interest = document.querySelector('#interest');
  const requestedInterest = new URLSearchParams(window.location.search).get('interest');
  if (requestedInterest && Array.from(interest.options).some(option => option.value === requestedInterest)) {
    interest.value = requestedInterest;
  }
  enquiryForm.addEventListener('submit', event => {
    event.preventDefault();
    if (!enquiryForm.reportValidity()) return;
    const fields = new FormData(enquiryForm);
    const subject = fields.get('interest') || 'General Enquiry';
    const body = `Name: ${fields.get('name')}\nEmail: ${fields.get('email')}\nOrganisation: ${fields.get('organisation')}\nArea of interest: ${subject}\n\n${fields.get('message')}`;
    const status = document.querySelector('#form-status');
    status.textContent = 'Your enquiry is ready in an email draft. Review and send it in your email app. If no app opens, email info@frontiersexec.org directly.';
    window.location.href = `mailto:info@frontiersexec.org?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });
}
