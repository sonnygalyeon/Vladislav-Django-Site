document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.login-form');
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const errorUsername = document.getElementById('username-error');
    const errorPassword = document.getElementById('password-error');

    form.addEventListener('submit', function(event) {
        let valid = true;

        // Сбросить сообщения об ошибках
        errorUsername.textContent = '';
        errorPassword.textContent = '';

        if (username.value.trim() === '') {
            errorUsername.textContent = 'Имя пользователя обязательно!';
            valid = false;
        }

        if (password.value.trim() === '') {
            errorPassword.textContent = 'Пароль обязателен!';
            valid = false;
        }

        if (!valid) {
            event.preventDefault(); // Предотвратить отправку формы, если есть ошибки
        }
    });
});