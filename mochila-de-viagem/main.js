const form = document.getElementById("novoItem");
const listaAtual = document.getElementById("listaItens");

const AddItem = (fnome, fquantidade) => {
    const novoItem = document.createElement("li");
    novoItem.classList.add("item");

    const numItem = document.createElement("strong");
    numItem.innerHTML = fquantidade;

    novoItem.appendChild(numItem);
    novoItem.innerHTML += fnome;
    listaAtual.appendChild(novoItem);
};

const itens =
    JSON.parse(localStorage.getItem("item")) == null
        ? []
        : JSON.parse(localStorage.getItem("item"));



itens.map((mItem) => {
    AddItem(mItem.nome, mItem.quantidade);
});


const guardainformação = (fnome, fquantidade) => {
    AddItem(fnome, fquantidade);

    const itemAtual = {
        nome: fnome,
        quantidade: fquantidade,
    };
    itens.push(itemAtual);

    localStorage.setItem("item", JSON.stringify(itens));
};

form.addEventListener("submit", (event) => {
    event.preventDefault();
    const nomeItem = event.target.elements["nome"];
    const quantItem = event.target.elements["quantidade"];
    guardainformação(nomeItem.value, quantItem.value);
    nomeItem.value = "";
    quantItem.value = "";
});
