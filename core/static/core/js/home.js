// static/core/js/index.js

document.addEventListener('DOMContentLoaded', function() {

    // (Seu código do menu hambúrguer já está aqui)
    // ...

    // --- LÓGICA PARA O CARROSSEL DE BANNERS ---

    // 1. Seleciona os elementos HTML
    const slides = document.querySelectorAll('.slides img');
    const indicadores = document.querySelectorAll('.indicadores span');
    let slideAtual = 0;

    // Garante que o código só execute se houver slides na página
    if (slides.length > 0) {

        // 2. Função para mostrar um slide específico
        function mostrarSlide(index) {
            // Esconde todos os slides e desativa todos os indicadores
            slides.forEach((slide, i) => {
                slide.classList.remove('active');
                if (indicadores[i]) indicadores[i].classList.remove('ativo');
            });
            // Mostra o slide e ativa o indicador correspondente
            slides[index].classList.add('active');
            if (indicadores[index]) indicadores[index].classList.add('ativo');
        }

        // 3. Função para avançar para o próximo slide
        function proximoSlide() {
            // Calcula o índice do próximo slide, voltando ao primeiro se chegar no fim
            slideAtual = (slideAtual + 1) % slides.length;
            mostrarSlide(slideAtual);
        }

        // 4. O temporizador: chama a função proximoSlide() a cada 5 segundos (5000 milissegundos)
        setInterval(proximoSlide, 5000);

        // (Bônus) Permite que o usuário clique nos indicadores para mudar de slide
        indicadores.forEach((indicador, index) => {
            indicador.addEventListener('click', () => {
                mostrarSlide(index);
                slideAtual = index; // Atualiza o slide atual para o temporizador continuar do ponto certo
            });
        });
    }

});