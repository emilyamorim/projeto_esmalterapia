//CÓDIGO DO MENU LATERAL

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




//CÓDIGO DOS SLIDES

document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll(".slides img");
    const indicators = document.querySelectorAll(".indicadores span");
    let currentIndex = 0; // Índice da imagem atual
    const intervalTime = 3000; // Tempo de troca (3 segundos)
    
    function showSlide(index) {
        // Esconde todas as imagens e remove a classe 'ativo' dos indicadores
        slides.forEach(slide => slide.classList.remove("active"));
        indicators.forEach(indicator => indicator.classList.remove("ativo"));

        // Mostra a imagem correspondente e ativa o indicador
        slides[index].classList.add("active");
        indicators[index].classList.add("ativo");
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length; // Vai para o próximo slide
        showSlide(currentIndex);
    }

    // Evento de clique nos indicadores
    indicators.forEach((indicator, index) => {
        indicator.addEventListener("click", () => showSlide(index));
    });

    // Inicialização
    showSlide(0);
    setInterval(nextSlide, intervalTime);
});




//CÓDIGO DA PROMOÇÃO 24H

const countDownDate = new Date().getTime() + 24 * 60 * 60 * 1000;

// Atualiza o contador a cada segundo
const countdownFunction = setInterval(() => {
    const now = new Date().getTime();
    const distance = countDownDate - now;

    // Calcula horas, minutos e segundos
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)); // Corrigido aqui
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Exibe o resultado no elemento com id="countdown"
    document.getElementById("hours").innerHTML = String(hours).padStart(2, "0");
    document.getElementById("minutes").innerHTML = String(minutes).padStart(2, "0");
    document.getElementById("seconds").innerHTML = String(seconds).padStart(2, "0");

    // Se o contador chegar a zero, exibe uma mensagem
    if (distance < 0) {
        clearInterval(countdownFunction);
        document.getElementById("countdown").innerHTML = "Promoção encerrada!";
    }
}, 1000);