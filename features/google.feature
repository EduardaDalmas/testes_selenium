# language:pt
Funcionalidade: fazer uma busca no Google

    Contexto: acessar a página para o teste
        Dado que acesso a página do Google 
    
    Cenário: acesssar a página do Google e fazer uma busca
        Dado que eu preencho a barra de pesquisar com Grêmio
        Quando eu clicar no botão de pesquisar
        Então devo visualizar os resultados da pesquisa
        