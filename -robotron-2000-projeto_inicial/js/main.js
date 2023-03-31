const arrayBotoes = Array.from(document.querySelectorAll(".controle-ajuste"));

arrayBotoes.map((botoes) => {
  botoes.addEventListener("click", (evento) => {
    const ids = evento.target.id.split("_");
    const componente = ids[0];
    const componenteInput = document.querySelector(`#${componente}_Input`);
    const operacao = ids[1];

    operacao == "subtrai"
      ? parseInt(componenteInput.value) > 0 &&
        (componenteInput.value = parseInt(componenteInput.value) - 1)
      : operacao == "soma" &&
        (componenteInput.value = parseInt(componenteInput.value) + 1);
  });
});

// const subtrair = document.querySelector("#subtrai");
// const somar = document.querySelector("#soma");
// const braco = document.querySelector("#bracoInput");

// const ClicarFunction = (objeto, funcao)=>{
//     objeto.addEventListener("click", funcao);
// }

// ClicarFunction(subtrair, ()=>{parseInt(braco.value) > 0 && (braco.value = parseInt(braco.value) - 1)})
// ClicarFunction(somar, ()=>{braco.value = parseInt(braco.value) + 1})
