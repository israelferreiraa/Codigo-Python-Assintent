import re

# AtendeAI - Assistente Inteligente de Atendimento
# Protótipo desenvolvido para fins acadêmicos.

def classificar_mensagem(mensagem):
    """Identifica o assunto com base em palavras-chave."""
    texto = mensagem.casefold()

    categorias = {
        "Financeiro": ["financeiro", "financeira", "financeiros", "financeiras",
                       "pagamento", "pagamentos", "boleto", "boletos",
                       "fatura", "faturas", "cobrança", "cobranças"],
        "Pedidos": ["pedido", "pedidos", "entrega", "entregas",
                    "produto", "produtos", "encomenda", "encomendas"],
        "Suporte técnico": ["suporte técnico", "suporte", "erro", "erros",
                            "sistema", "sistemas",
                            "senha", "senhas", "acesso", "acessos"],
        "Informações gerais": ["informações gerais", "informação geral",
                               "horário", "horários", "endereço", "endereços",
                               "funcionamento"]
    }

    for categoria, palavras in categorias.items():
        if any(re.search(rf"\b{re.escape(palavra)}\b", texto) for palavra in palavras):
            return categoria

    return "Atendimento humano"


def gerar_resposta(categoria):
    """Retorna uma sugestão de resposta para cada categoria."""
    respostas = {
        "Financeiro": (
            "Vamos ajudar com sua solicitação financeira. "
            "Verifique os dados do pagamento."
        ),
        "Pedidos": (
            "Vamos verificar as informações do seu pedido "
            "e orientar sobre a entrega."
        ),
        "Suporte técnico": (
            "Vamos analisar o problema técnico informado "
            "e orientar sobre os próximos passos."
        ),
        "Informações gerais": (
            "Podemos ajudar com informações sobre nossos serviços."
        ),
        "Atendimento humano": (
            "Sua solicitação precisa de análise individual. "
            "Encaminhe a mensagem para um atendente."
        )
    }

    return respostas[categoria]


def atender_cliente(mensagem):
    """Processa a mensagem e organiza o resultado."""
    categoria = classificar_mensagem(mensagem)
    resposta = gerar_resposta(categoria)

    print("\n--- Resultado do AtendeAI ---")
    print(f"Mensagem recebida: {mensagem}")
    print(f"Categoria identificada: {categoria}")
    print(f"Resposta sugerida: {resposta}")

    if categoria == "Atendimento humano":
        print("Ação: encaminhar para um atendente.")
    else:
        print("Ação: apresentar a sugestão para revisão.")


def executar():
    """Executa o atendimento até o usuário encerrar."""
    print("Bem-vindo ao AtendeAI!")
    print("Digite 'sair' a qualquer momento para encerrar.")

    while True:
        mensagem = input("\nDigite sua mensagem: ").strip()

        if mensagem.lower() == "sair":
            print("Atendimento encerrado.")
            break

        if not mensagem:
            print("Digite uma mensagem válida.")
            continue

        atender_cliente(mensagem)

        while True:
            continuar = input("\nDeseja continuar o atendimento? (s/n): ").strip().casefold()

            if continuar in {"s", "sim", "continuar"}:
                break

            if continuar in {"n", "não", "nao", "sair"}:
                print("Atendimento encerrado.")
                return

            print("Resposta inválida. Digite 's' para continuar ou 'n' para encerrar.")


if __name__ == "__main__":
    executar()