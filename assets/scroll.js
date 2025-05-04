document.addEventListener("DOMContentLoaded", function () {
    // Botão de alternância
    const toggleButton = document.getElementById("navbar-toggle");
    const linksContainer = document.getElementById("navbar-links");

    if (toggleButton && linksContainer) {
        toggleButton.addEventListener("click", function () {
            linksContainer.classList.toggle("show"); // Alterna a classe "show"
        });
    }

    // Links de navegação
    const links = document.querySelectorAll(".nav-link");
    const navbar = document.querySelector(".navbar-container");
    const navbarHeight = navbar ? navbar.offsetHeight : 0; // Evita erro se navbar não existir

    if (links.length > 0) {
        links.forEach(link => {
            link.addEventListener("click", function (event) {
                const targetId = this.getAttribute("href")?.substring(1);
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    event.preventDefault();
                    window.scrollTo({
                        top: targetElement.offsetTop - navbarHeight - 10,
                        behavior: "smooth",
                    });
                }
            });
        });
    }
});
