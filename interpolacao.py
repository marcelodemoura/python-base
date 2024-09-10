email_tmpl = """
    Olá, %(nome)s
    
    Tem interesse em comprar %(produto)s?
    
    %(texto)s
    
    clique agora no %(link)s
    
    Apenas %(quantidades)d disponiveis!
    
    Preço promocional %(preco).2f
    """
for cliente in clientes:
    print (
        email_tmpl
            % {
                "nome": cliente,
                "produto": "caneta",
                "texto": "Escreve muito bem",
                "link": "https://cantaslegais.com",
                "quantidade": 1,
                "preco": 50.5,
    }
)