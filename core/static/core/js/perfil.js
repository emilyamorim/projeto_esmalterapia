// static/core/js/perfil.js
document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('.tab-link');
    const contents = document.querySelectorAll('.tab-content');

    // Função para ativar uma aba
    function activateTab(tabId) {
        // Esconde todos os conteúdos e desativa todas as abas
        contents.forEach(content => {
            content.classList.remove('active');
        });
        tabs.forEach(tab => {
            tab.classList.remove('active');
        });

        // Encontra o conteúdo e a aba correspondente ao ID e os ativa
        const targetContent = document.getElementById(tabId);
        const targetTab = document.querySelector(`.tab-link[data-tab="${tabId}"]`);

        if (targetContent) {
            targetContent.classList.add('active');
        }
        if (targetTab) {
            targetTab.classList.add('active');
        }
    }

    // Adiciona o evento de clique a cada botão de aba
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetId = tab.getAttribute('data-tab');
            activateTab(targetId);
        });
    });

    // Garante que a primeira aba ("Dados Pessoais") esteja ativa ao carregar a página
    activateTab('dados-pessoais');
});