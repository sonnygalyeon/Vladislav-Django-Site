document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector('.register-form');
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm-password');

    const errorUsername = document.getElementById('username-error');
    const errorEmail = document.getElementById('email-error');
    const errorPassword = document.getElementById('password-error');
    const errorConfirmPassword = document.getElementById('confirm-password-error');

    form.addEventListener('submit', function (event) {
        let valid = true;

        // Сброс сообщений об ошибках
        errorUsername.textContent = '';
        errorEmail.textContent = '';
        errorPassword.textContent = '';
        errorConfirmPassword.textContent = '';

        if (username.value.trim() === '') {
            errorUsername.textContent = 'Имя пользователя обязательно!';
            valid = false;
        }

        if (email.value.trim() === '') {
            errorEmail.textContent = 'Электронная почта обязательна!';
            valid = false;
        }

        if (password.value.length < 6) {
            errorPassword.textContent = 'Пароль должен содержать минимум 6 символов!';
            valid = false;
        }

        if (password.value !== confirmPassword.value) {
            errorConfirmPassword.textContent = 'Пароли не совпадают!';
            valid = false;
        }

        if (!valid) {
            event.preventDefault(); // Предотвращаем отправку формы
        }
    });
});