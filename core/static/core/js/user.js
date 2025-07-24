function openTab(event, tabId) {
    document.querySelectorAll(".tab-content").forEach(tab => {
        tab.classList.remove("active");
    });

    document.querySelectorAll(".tab-button").forEach(button => {
        button.classList.remove("active");
    });

    document.getElementById(tabId).classList.add("active");
    event.currentTarget.classList.add("active");
}

// Máscaras e Validações
document.addEventListener("DOMContentLoaded", function () {
    // Máscara do CPF
    const cpfField = document.getElementById('cpf');
    if (cpfField) {
        cpfField.addEventListener('input', function (e) {
            e.target.value = e.target.value
                .replace(/\D/g, "")
                .replace(/(\d{3})(\d)/, "$1.$2")
                .replace(/(\d{3})(\d)/, "$1.$2")
                .replace(/(\d{3})(\d{1,2})$/, "$1-$2");
        });
    }

    // Máscara do Telefone
    const telefoneField = document.getElementById('telefone');
    if (telefoneField) {
        telefoneField.addEventListener('input', function (e) {
            let value = e.target.value.replace(/\D/g, '');
            value = value.replace(/(\d{2})(\d)/, '($1) $2');
            value = value.replace(/(\d{5})(\d{4})/, '$1-$2');
            e.target.value = value.substring(0, 15);
        });
    }

    // Configurar data máxima
    const dataNascimentoField = document.getElementById('data_nascimento');
    if (dataNascimentoField) {
        dataNascimentoField.max = new Date().toISOString().split("T")[0];
    }
});

// Função principal de validação
function validar(event) {
    event.preventDefault();
    resetErros();
    
    let isValid = true;
    const statusDiv = document.getElementById('validacao-status');
    if (statusDiv) statusDiv.classList.remove('valido', 'invalido');

    // Validação do Nome
    const nome = document.getElementById('nome').value.trim();
    if (!nome) {
        showError('nome', 'Nome é obrigatório');
        isValid = false;
    } else if (nome.length < 2) {
        showError('nome', 'Mínimo 2 caracteres');
        isValid = false;
    }

    // Validação do Sobrenome
    const sobrenome = document.getElementById('sobrenome').value.trim();
    if (!sobrenome) {
        showError('sobrenome', 'Sobrenome é obrigatório');
        isValid = false;
    }

    // Validação do CPF
    const cpf = document.getElementById('cpf').value;
    if (!validarCPF(cpf)) {
        showError('cpf', 'CPF inválido');
        isValid = false;
    }

    // Validação do Email
    const email = document.getElementById('email').value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showError('email', 'Email inválido');
        isValid = false;
    }

    // Validação do Telefone
    const telefone = document.getElementById('telefone').value;
    const telefoneRegex = /^\(\d{2}\) \d{5}-\d{4}$/;
    if (!telefoneRegex.test(telefone)) {
        showError('telefone', 'Telefone inválido');
        isValid = false;
    }

    // Validação da Data de Nascimento
    const dataInput = document.getElementById('data_nascimento');
    const dataNasc = new Date(dataInput.value);
    const hoje = new Date();
    if (dataNasc > hoje) {
        showError('data', 'Data futura inválida');
        isValid = false;
    }

    // Feedback final
    if (statusDiv) {
        if (isValid) {
            statusDiv.textContent = '✓ Todos os campos estão válidos!';
            statusDiv.classList.add('valido');
            setTimeout(() => {
                statusDiv.classList.remove('valido');
                statusDiv.textContent = '';
            }, 5000);
        } else {
            statusDiv.textContent = '⚠ Por favor, corrija os campos destacados';
            statusDiv.classList.add('invalido');
        }
    }

    return isValid;
}

// Função de validação do CPF
function validarCPF(cpf) {
    cpf = cpf.replace(/\D/g, '');
    if (cpf.length !== 11 || /^(\d)\1{10}$/.test(cpf)) return false;

    let soma = 0, resto;
    for (let i = 1; i <= 9; i++) soma += parseInt(cpf[i-1]) * (11 - i);
    resto = (soma * 10) % 11;
    if ((resto === 10 || resto === 11)) resto = 0;
    if (resto !== parseInt(cpf[9])) return false;

    soma = 0;
    for (let i = 1; i <= 10; i++) soma += parseInt(cpf[i-1]) * (12 - i);
    resto = (soma * 10) % 11;
    if ((resto === 10 || resto === 11)) resto = 0;
    if (resto !== parseInt(cpf[10])) return false;

    return true;
}

// Funções auxiliares
function showError(campo, mensagem) {
    const erroElement = document.getElementById(`erro-${campo}`);
    if (erroElement) {
        erroElement.textContent = mensagem;
        erroElement.style.color = 'red';
    }
}

function resetErros() {
    document.querySelectorAll('.erro').forEach(erro => {
        erro.textContent = '';
    });
}

// Código do Menu Lateral
document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.querySelector(".menu-hamburguer");
    const mobileMenu = document.querySelector(".mobile-menu");
    const closeBtn = document.querySelector(".close-menu");
    const overlay = document.querySelector(".overlay");

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener("click", function () {
            mobileMenu.classList.add("menu-aberto");
            overlay.classList.add("active");
        });
    }

    function fecharMenu() {
        mobileMenu.classList.remove("menu-aberto");
        overlay.classList.remove("active");
        document.querySelectorAll(".dropdown-menu").forEach(menu => {
            menu.style.display = "none";
        });
        document.querySelectorAll(".dropdown").forEach(dropdown => {
            dropdown.classList.remove("open");
        });
    }

    if (closeBtn) closeBtn.addEventListener("click", fecharMenu);
    if (overlay) overlay.addEventListener("click", fecharMenu);
});