document.addEventListener("DOMContentLoaded", function() {
  const entrada = document.getElementById("entrada");
  const contador = document.getElementById("contador");

  // 🔹 Sempre limpa o campo ao carregar/recarregar a página
  entrada.value = "";
  contador.textContent = "Caracteres: 0";

  // Atualiza contador em tempo real
  entrada.addEventListener("input", function() {
    contador.textContent = "Caracteres: " + entrada.value.length;
  });

  // Clique nos últimos pedidos
  document.querySelectorAll(".pedido-item").forEach(function(item) {
    item.addEventListener("click", function() {
      let texto = this.getAttribute("data-texto");
      entrada.value = texto;
      contador.textContent = "Caracteres: " + texto.length;

      // Remove resposta e aviso
      let respostaDiv = document.querySelector(".alert");
      if (respostaDiv) respostaDiv.remove();
      document.getElementById("aviso-curto").innerHTML = "";
    });
  });

  // Clique no botão enviar
  const btnEnviar = document.getElementById("btn-enviar");
  btnEnviar.addEventListener("click", function(event) {
    const texto = entrada.value.trim();

    // Limpa resposta e aviso antes de validar
    let respostaDiv = document.querySelector(".alert");
    if (respostaDiv) respostaDiv.remove();
    document.getElementById("aviso-curto").innerHTML = "";

    // Validação
    if (texto.length === 0) {
      event.preventDefault();
      document.getElementById("aviso-curto").innerHTML =
        `<div class="alert alert-danger mt-2">
           Preencha o campo da mensagem antes de enviar.
         </div>`;
    } else if (texto.length < 50) {
      event.preventDefault();
      document.getElementById("aviso-curto").innerHTML =
        `<div class="alert alert-warning mt-2">
           A mensagem possui <strong>${texto.length}</strong> caracteres e é muito curta para ser processada.
           Digite pelo menos 50 caracteres.
         </div>`;
    }
  });
});
