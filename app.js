window.addEventListener(
    'DOMContentLoaded', function () {
        const overlay = document.querySelector('#overlay')
        const signupBtn = document.querySelector('#signup-btn')
        const closeBtn = document.querySelector('#close-btn')
        const overlayLogin = document.querySelector("#overlay-login")
        const loginBtn = document.querySelector("#login-btn")
        const closeBtnLogin = document.querySelector("#close-btn-login")

        signupBtn.addEventListener('click', function() {
            overlay.classList.remove('hidden')
            overlay.classList.add('flex')
        })

        closeBtn.addEventListener('click', function() {
            overlay.classList.remove('flex')
            overlay.classList.add('hidden')
        })

        loginBtn.addEventListener('click', function() {
            overlayLogin.classList.remove('hidden')
            overlayLogin.classList.add('flex')
        })

        closeBtnLogin.addEventListener('click', function() {
            overlayLogin.classList.remove('flex')
            overlayLogin.classList.add('hidden')
        })

    }
<<<<<<< HEAD
<<<<<<< HEAD
)
=======
)

>>>>>>> login-backend
=======

>>>>>>> 4adb892f93db09cea01c9682603ff9f9bbc35cb1
