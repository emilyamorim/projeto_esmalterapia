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
        // Adiciona as classes 'ativo' que fazem os elementos aparecerem (conforme definido no CSS)
        if (mobileMenu) mobileMenu.classList.add('menu-aberto');
        if (overlay) overlay.classList.add('active');
    }

    // Função para fechar o menu
    function fecharMenu() {
        // Remove as classes 'ativo', fazendo os elementos desaparecerem
        if (mobileMenu) mobileMenu.classList.remove('menu-aberto');
        if (overlay) overlay.classList.remove('active');
    }

    // 2. Adiciona os "escutadores de eventos" de clique
    // Se o ícone hamburguer for clicado, chama a função para abrir o menu
    if (menuHamburguer) {
        menuHamburguer.addEventListener('click', abrirMenu);
    }

    // Se o botão de fechar ('X') for clicado, chama a função para fechar o menu
    if (closeMenu) {
        closeMenu.addEventListener('click', fecharMenu);
    }

    // Se a área escura (overlay) for clicada, também fecha o menu
    if (overlay) {
        overlay.addEventListener('click', fecharMenu);
    }

     // --- INÍCIO DA NOVA LÓGICA DO ACORDEÃO ---
     const dropdownToggles = document.querySelectorAll('.mobile-menu .dropdown-toggle');

     dropdownToggles.forEach(toggle => {
         toggle.addEventListener('click', function(event) {
             // event.preventDefault() impede que o link '#' recarregue a página
             event.preventDefault();
 
             // Pega o elemento <li> que é o "pai" do link clicado
             const parentLi = this.parentElement;
 
             // Adiciona ou remove a classe 'open' do <li>
             // É essa classe que o CSS usa para mostrar ou esconder o submenu
             parentLi.classList.toggle('open');
         });
     });
     // --- FIM DA NOVA LÓGICA DO ACORDEÃO ---

    // --- FIM DA LÓGICA DO MENU ---


    // --- LÓGICA DO CARROSSEL (pode ser adicionada aqui) ---

});