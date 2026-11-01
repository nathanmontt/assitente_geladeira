# GELY - Assistente de Geladeira Inteligente (CLI)

Um programa de terminal desenvolvido em Python para cadastrar e organizar receitas culinárias. O sistema permite criar receitas associadas a conjuntos de ingredientes, garantindo que não haja ingredientes repetidos dentro da mesma receita.

## Funcionalidades Atuais

- **Personalização de usuário:** boas-vindas personalizadas com validação de nome (impedindo entradas vazias ou contendo números).
- **Cadastro de receitas e ingredientes:** permite adicionar o nome da receita e múltiplos ingredientes de forma interativa.
- **Filtro de ingredientes únicos (set):** os ingredientes de cada receita são armazenados em um set(), impedindo duplicações de um mesmo ingrediente.
- **Estruturação de dados híbrida:** cada receita é empacotada em uma Tupla (nome_da_receita, set_de_ingredientes) e armazenada dentro da Lista principal de receitas.
- **Visualização completa:** exibição clara e numerada de todas as receitas cadastradas e seus respectivos ingredientes.

## *Feats* Futuras

- [ ] **Busca por ingredientes disponíveis:** verificar quais ingredientes o usuário possui na geladeira e sugerir receitas possíveis utilizando operações de conjuntos (issubset / intersecção).
- [ ] **Busca por receitas dispoíveis:** permitir buscar receitas já cadastradas, via nome da mesma.
- [ ] **Remoção e edição de receitas:** permitir excluir ou modificar receitas já cadastradas.
- [x] **Exportação para PDF:** gerar um livro de receitas em formato PDF utilizando a biblioteca reportlab.

## Pré-requisitos

Para rodar este projeto, você precisa ter o Python 3.10 ou superior instalado no seu computador, pois o código utiliza a estrutura moderna de controle de fluxo match/case.

## Como clonar e executar para uso próprio

Se você quiser testar este projeto na sua máquina, siga os passos abaixo:

1. Abra o seu terminal (ou Git Bash).
2. Clone este repositório executando o comando:
   ```bash
   git clone https://https://github.com/nathanmontt/assitente_geladeira.git
3. Execute o arquivo Python:
   ```bash
   python assitente_geladeira.py