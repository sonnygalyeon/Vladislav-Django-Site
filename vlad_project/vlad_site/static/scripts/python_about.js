function runCode() {
    const output = document.getElementById('output');
    output.textContent = '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]';
    output.classList.add('animate');
    setTimeout(() => output.classList.remove('animate'), 500);
}

function toggleTheme() {
    document.body.dataset.theme =
        document.body.dataset.theme === 'dark' ? 'light' : 'dark';
}

// Анимация для элементов при прокрутке
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = 1;
            entry.target.style.transform = 'translateY(0)';
        }
    });
});

document.querySelectorAll('section').forEach((section) => {
    section.style.opacity = 0;
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'all 0.6s ease-out';
    observer.observe(section);
});