const caixa = document.getElementById("caixa");
const chkDestaque = document.getElementById("chkDestaque");
const corTexto = document.getElementById("corTexto");
const tamanhoFonte = document.getElementById("tamanhoFonte");
const valorFonte = document.getElementById("valorFonte");
const btnRestaurar = document.getElementById("btnRestaurar");

chkDestaque.addEventListener("change", alterarDestaque);
corTexto.addEventListener("change", alterarCor);
tamanhoFonte.addEventListener("input", alterarTamanhoFonte);
btnRestaurar.addEventListener("click", restaurarPadrao);

function alterarDestaque() {
    if (chkDestaque.checked) {
        caixa.style.backgroundColor = "yellow";
        caixa.style.fontWeight = "bold";
    } else {
        caixa.style.backgroundColor = "";
        caixa.style.fontWeight = "";
    }
}

function alterarCor() {
    caixa.style.color = corTexto.value;
}

function alterarTamanhoFonte() {
    caixa.style.fontSize = tamanhoFonte.value + "px";
    valorFonte.innerText = tamanhoFonte.value + "px";
}

function restaurarPadrao() {
    caixa.style.backgroundColor = "";
    caixa.style.fontWeight = "";
    caixa.style.color = "black";
    caixa.style.fontSize = "20px";

    chkDestaque.checked = false;
    corTexto.value = "black";
    tamanhoFonte.value = 20;
    valorFonte.innerText = "20px";
}