# Finodromo

Bem-vindo ao Finodromo!

## 📖 Introdução

O Finodromo é um repositório colaborativo onde calouros de Ciência da Computação podem compartilhar provas (“finas”) das disciplinas que já cursaram. Para manter a organização, utilizamos um script Python que gera automaticamente a estrutura de pastas.

---

## 🗂️ Estrutura de Pastas Automática

A partir do arquivo `disciplinas.txt`, o script `create_structure.py` cria automaticamente:

```
decom/
demat/
outras/
```

E, dentro de cada categoria, pastas das disciplinas, professores e subpastas `Provas/` e `Material/`.

> **IMPORTANTE:**  
> - **NÃO** crie manualmente pastas de disciplina nem de professor.  
> - **APENAS** pastas de período (`<ANO>.<PERIODO>`, ex: `25.1`) podem ser criadas manualmente.

### Formato do `disciplinas.txt`

O arquivo deve seguir este padrão, em blocos separados por linha em branco:

```
<CÓDIGO DA DISCIPLINA>
-NOME DA DISCIPLINA
--NOME DO PROFESSOR 1
--NOME DO PROFESSOR 2 (opcional)
```

Exemplo:

```
BCC501
-INTRODUCAO A CIENCIA DA COMPUTACAO
--Saul Emanuel Delabrida Silva

MTM122
-CALCULO DIFERENCIAL E INTEGRAL I
```

---

## 🚀 Como Contribuir (Passo a Passo)

**Siga estes passos com atenção**! Coloque imagens futuramente onde indicado para facilitar.

### 1. Pré-requisitos

1. Git instalado (verifique com `git --version`).  
2. Python 3 instalado (verifique com `python3 --version`).  
3. Uma conta no GitHub.

### 2. Clonar o Repositório

1. Abra o terminal (ou Git Bash no Windows).  
2. Navegue até a pasta onde quer guardar o projeto.  
3. Execute:
   ```bash
   git clone https://github.com/SEU_USUARIO/finodromo.git
   ```
4. Entre na pasta do projeto:
   ```bash
   cd finodromo
   ```
5. <!-- FUTURAMENTE: ![Passo 2 – Clonar repositório](docs/images/clone.png) -->

### 3. Executar o Script de Estrutura

1. Verifique se `disciplinas.txt` está na raiz do repositório.  
2. Execute:
   ```bash
   python3 create_structure.py
   ```
3. Aguarde a mensagem:
   ```
   ✅ Estrutura de pastas criada com sucesso.
   ```
4. <!-- FUTURAMENTE: ![Passo 3 – Executar script](docs/images/run_script.png) -->

### 4. Criar Pasta de Período Manualmente (Somente se Necessário)

> **Atenção:** somente pastas de período `<ANO>.<PERIODO>` podem ser criadas manualmente.

1. Dentro da pasta do professor, crie uma pasta com o período da prova.  
   Exemplo:
   ```
   decom/BCC501 - INTRODUCAO A CIENCIA DA COMPUTACAO/Saul Emanuel Delabrida Silva/25.1/
   ```

### 5. Adicionar a Fina

1. Copie o arquivo da prova para dentro da pasta de período criada.  
2. Renomeie o arquivo para:
   ```
   prova1.<extensão>
   ```
   Exemplos: `prova1.pdf`, `prova1.png`  
3. **Importante:** se o nome do arquivo ou o diretório de período não estiver no formato correto, seu Pull Request será **NEGADO**.

### 6. Commit e Push das Alterações

1. Verifique o status:
   ```bash
   git status
   ```
2. Adicione os arquivos:
   ```bash
   git add .
   ```
3. Crie um branch descritivo:
   ```bash
   git checkout -b adiciona-fina-BCC501-25.1
   ```
4. Faça o commit:
   ```bash
   git commit -m "Adiciona prova BCC501 25.1 para Saul Emanuel"
   ```
5. Envie para o GitHub:
   ```bash
   git push origin adiciona-fina-BCC501-25.1
   ```

### 7. Abrir um Pull Request

1. Acesse o repositório no GitHub.  
2. Clique em **Compare & pull request**.  
3. Preencha:
   - **Título:** breve e descritivo.  
   - **Descrição:** explique o que adicionou e confira as regras.  
4. Clique em **Create pull request**.

---

## 📌 Regras de Validação

- Disciplinas com código contendo `BCC` ➡️ `decom/`  
- Disciplinas com `MTM` ➡️ `demat/`  
- Demais ➡️ `outras/`  
- Pastas de disciplina e professor são geradas **automaticamente** pelo script.  
- **Somente** pastas de período `<ANO>.<PERIODO>` podem ser criadas manualmente.  
- Arquivos de prova devem se chamar `prova1.<extensão>`.  
- Pull Requests que não seguirem o formato serão **NEGADOS**.

---

Pronto! Agora você já sabe como contribuir com o Finodromo. Boas contribuições! 🎉
