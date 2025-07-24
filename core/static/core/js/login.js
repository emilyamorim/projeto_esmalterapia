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


//Autenticar Login
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(e) {
        e.preventDefault(); // Previne o recarregamento da página

        // Obtém os valores dos inputs
        const email = document.getElementById('email').value.trim();
        const senha = document.querySelector('input[name="senha"]').value;

        // Verifica se os campos não estão vazios
        if (!email || !senha) {
            alert("Preencha todos os campos!");
            return;
        }

        // Recupera os usuários armazenados no localStorage
        const usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];

        // Procura o usuário com o e-mail informado
        const usuarioEncontrado = usuarios.find(user => user.email === email);

        // Se não encontrar ou se a senha estiver incorreta, exibe mensagem genérica de erro
        if (!usuarioEncontrado || usuarioEncontrado.senha !== senha) {
            alert("E-mail ou senha inválidos!");
            return;
        }

        // Armazena o usuário na sessão
        sessionStorage.setItem('usuarioLogado', JSON.stringify(usuarioEncontrado));

        // Redireciona com base no tipo de usuário
        if (usuarioEncontrado.tipo === 'admin') {
            window.location.href = "admin.html";
        } else {
            window.location.href = "pagina_principal_logada.html";
        }
    });
});
