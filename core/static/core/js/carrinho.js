document.addEventListener("DOMContentLoaded", function () {
    const produtos = document.querySelectorAll(".esmaltes");
    const menuBtn = document.querySelector(".menu-hamburguer");
    const mobileMenu = document.querySelector(".mobile-menu");
    const closeBtn = document.querySelector(".close-menu");
    const overlay = document.querySelector(".overlay");

    produtos.forEach(produto => {
        const botaoMenos = produto.querySelector(".botao-menos");
        const botaoMais = produto.querySelector(".botao-mais");
        const inputQuantidade = produto.querySelector(".quantidade-input");

        
        botaoMais.addEventListener("click", function () {
            inputQuantidade.value = parseInt(inputQuantidade.value) + 1;
        });

        
        botaoMenos.addEventListener("click", function () {
            if (parseInt(inputQuantidade.value) > 1) {
                inputQuantidade.value = parseInt(inputQuantidade.value) - 1;
            }
        });
    });

    // ABRIR MENU LATERAL AO CLICAR NO MENU HAMBÚRGUER
    menuBtn.addEventListener("click", function () {
        mobileMenu.classList.add("menu-aberto");
        overlay.classList.add("active");
    });

    // FECHAR MENU LATERAL
    closeBtn.addEventListener("click", function () {
        fecharMenu();
    });

    overlay.addEventListener("click", function () {
        fecharMenu();
    });

    // FUNÇÃO PARA FECHAR O MENU LATERAL E TODOS OS DROPDOWNS
    function fecharMenu() {
        mobileMenu.classList.remove("menu-aberto");
        overlay.classList.remove("active");

        // Fechar todos os dropdowns ao fechar o menu
        document.querySelectorAll(".dropdown-menu").forEach(menu => {
            menu.style.display = "none";
        });

        // Remover a classe "open" de todos os dropdowns
        document.querySelectorAll(".dropdown").forEach(dropdown => {
            dropdown.classList.remove("open");
        });
    }

});
