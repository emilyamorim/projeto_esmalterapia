// Garante que o script só rode depois que todo o HTML for carregado
document.addEventListener('DOMContentLoaded', function() {

    // --- LÓGICA PARA O CARROSSEL DE BANNERS ---
    
    // 1. Seleciona os elementos HTML do carrossel
    const slides = document.querySelectorAll('.slides .slide');
    const indicadores = document.querySelectorAll('.indicadores span');
    let slideAtual = 0;

    // Garante que o código só execute se houver slides na página
    if (slides.length > 0) {

        // 2. Função para mostrar um slide específico
        function mostrarSlide(index) {
            // Esconde todos os slides e desativa todos os indicadores
            slides.forEach((slide) => {
                slide.classList.remove('active');
            });
            indicadores.forEach((indicador) => {
                indicador.classList.remove('ativo');
            });
            
            // Mostra o slide e ativa o indicador correspondente
            slides[index].classList.add('active');
            indicadores[index].classList.add('ativo');
        }

        // 3. Função para avançar para o próximo slide
        function proximoSlide() {
            slideAtual = (slideAtual + 1) % slides.length;
            mostrarSlide(slideAtual);
        }

        // 4. O temporizador: chama a função proximoSlide() a cada 5 segundos
        setInterval(proximoSlide, 5000);

        // 5. Permite que o usuário clique nos indicadores
        indicadores.forEach((indicador, index) => {
            indicador.addEventListener('click', () => {
                mostrarSlide(index);
                slideAtual = index;
            });
        });
    }
});