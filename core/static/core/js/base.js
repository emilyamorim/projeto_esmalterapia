// Garante que o script só execute depois que todo o HTML da página for carregado
document.addEventListener('DOMContentLoaded', function() {

    // --- LÓGICA PARA O MENU HAMBÚRGUER ---
    
    // 1. Encontra os elementos HTML com os quais vamos interagir
    const menuHamburguer = document.querySelector('.menu-hamburguer');
    const mobileMenu = document.querySelector('.mobile-menu');
    const closeMenu = document.querySelector('.close-menu');
    const overlay = document.querySelector('.overlay');

    // Função para abrir o menu
    function abrirMenu() {
        if (mobileMenu) mobileMenu.classList.add('menu-aberto');
        if (overlay) overlay.classList.add('active');
    }

    // Função para fechar o menu
    function fecharMenu() {
        if (mobileMenu) mobileMenu.classList.remove('menu-aberto');
        if (overlay) overlay.classList.remove('active');
    }

    // 2. Adiciona os "escutadores de eventos" de clique
    if (menuHamburguer) {
        menuHamburguer.addEventListener('click', abrirMenu);
    }
    if (closeMenu) {
        closeMenu.addEventListener('click', fecharMenu);
    }
    if (overlay) {
        overlay.addEventListener('click', fecharMenu);
    }

    // --- LÓGICA DO ACORDEÃO INTERNO DO MENU ---
    const dropdownToggles = document.querySelectorAll('.mobile-menu .dropdown-toggle');

    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', function(event) {
            // event.preventDefault() impede que o link '#' recarregue a página
            event.preventDefault();

            // Pega o elemento <li> que é o "pai" do link clicado
            const parentLi = this.parentElement;

            // Adiciona ou remove a classe 'open' do <li>
            parentLi.classList.toggle('open');
        });
    });
});