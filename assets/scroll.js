document.addEventListener("DOMContentLoaded", function () {
    // Botão de alternância
    const toggleButton = document.getElementById("navbar-toggle");
    const linksContainer = document.getElementById("navbar-links");

    // Adiciona evento de clique ao botão
    toggleButton.addEventListener("click", function () {
        linksContainer.classList.toggle("show"); // Alterna a classe "show"
    });

    // Configura scroll suave ao clicar nos links
    const links = document.querySelectorAll(".nav-link");
    links.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100,  // Ajusta para compensar a altura do navbar
                    behavior: "smooth",
                });
            }
        });
    });
});
