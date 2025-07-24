document.querySelector("header").innerHTML = `
<header>
        <div class="logo">
            <img src="../image/logo_oficial_1.png" alt="Unhas Perfeitas">
        </div>
        <div class="menu-search-container">
            <nav>
                <ul class="nav-menu">
                    <li class="dropdown">
                        <a href="">Marcas</a>
                        <ul class="dropdown-menu">
                            <li class="marcas"><a href="">Rísque</a></li>
                            <li><a href="">Coloroma</a></li>
                            <li><a href="">Impala</a></li>
                            <li><a href="">Dailus</a></li>
                        </ul>
                    </li>

                    <li class="dropdown">
                        <a href="">Destaque</a>
                        <ul class="dropdown-menu">
                            <li><a href="">Produtos em Destaque</a></li>
                            <li><a href="">Novidades</a></li>
                            <li><a href="">Mais Vendidos</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
            <div class="search-bar">
                <input type="text" placeholder="Buscar">
                <button><i class="fi fi-rr-search"></i></button>
                <a href="carrinho.html"><i class="fi fi-rr-shopping-cart"></i></a>
                <a href="favoritos.html"><i class="fi fi-rr-heart"></i></a>
            </div>
        </div>

        <div class="menu-hamburguer">
            <div></div>
            <div></div>
            <div></div>
        </div>
    </header>

    <!--MENU EM MOBILE-->
    <div class="mobile-menu">
        <span class="close-menu"><i class="fi fi-rr-rectangle-xmark"></i></span>
        <ul>
            <li class="dropdown">
                <a href="#">Marcas</a>
                <ul class="dropdown-menu">
                    <li><a href="#">Rísque</a></li>
                    <li><a href="#">Colorama</a></li>
                    <li><a href="#">Impala</a></li>
                    <li><a href="#">Dailus</a></li>
                </ul>
            </li>
            <li class="dropdown">
                <a href="#">Destaque</a>
                <ul class="dropdown-menu">
                    <li><a href="#">Produtos em Destaque</a></li>
                    <li><a href="#">Novidades</a></li>
                    <li><a href="#">Mais Vendidos</a></li>
                </ul>
            </li>
        </ul>
    </div>

    <div class="overlay"></div>
`;

document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.querySelector(".menu-hamburguer");
    const mobileMenu = document.querySelector(".mobile-menu");
    const closeBtn = document.querySelector(".close-menu");
    const overlay = document.querySelector(".overlay");
    const dropdownToggles = document.querySelectorAll(".dropdown-toggle");

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
