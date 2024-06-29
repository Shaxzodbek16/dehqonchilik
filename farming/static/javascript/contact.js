// ixtiyoriy: Yuborish tugmasini bosganda animatsiya (masalan, rang o'zgarishi)
const submitButton = document.querySelector('button[type="submit"]');

submitButton.addEventListener('click', () => {
    submitButton.classList.add('submitting'); // CSSda .submitting klassi orqali animatsiya qo'shing
    setTimeout(() => {
        submitButton.classList.remove('submitting');
    }, 2000); // 2 soniya davomida animatsiya
});
