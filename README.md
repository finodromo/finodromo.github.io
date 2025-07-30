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

Onde estiver escrito <user> entenda como seu usuário do github.

### 1. Pré-requisitos

1. Git instalado (verifique com `git --version`).  
2. Python 3 instalado (verifique com `python3 --version`).  
3. Uma conta no GitHub.

### 2. Fork e configuração de remotes

1. No GitHub, faça **Fork** do repositório original:
   - Acesse `https://github.com/finodromo/finodromo.github.io`  
   - Clique em **Fork** (canto superior direito) e selecione sua conta (`<User>`).  

2. No terminal, dentro da pasta (caso já tenha clonado), renomeie o remote atual para `upstream`:
   ```bash
   git remote rename origin upstream
   ```

3. Adicione seu fork como `origin` (SSH):
   ```bash
   git remote add origin git@github.com:<user>/finodromo.github.io.git
   ```

4. Verifique os remotes:
   ```bash
   git remote -v
   ```
   Deve listar:
   ```
   origin    git@github.com:<user>/finodromo.github.io.git (fetch)
   origin    git@github.com:<user>/finodromo.github.io.git (push)
   upstream  git@github.com:finodromo/finodromo.github.io.git     (fetch)
   upstream  git@github.com:finodromo/finodromo.github.io.git     (push)
   ```

5. Se **ainda não** clonou, use:
   ```bash
   git clone git@github.com:<user>/finodromo.github.io.git
   cd finodromo.github.io
   ```

### 3. Clonar o Repositório (SSH)

1. Se não fez clone no passo anterior:
   ```bash
   git clone git@github.com:<user>/finodromo.github.io.git
   ```
2. Entre na pasta:
   ```bash
   cd finodromo.github.io
   ```

### 4. Executar o Script de Estrutura

1. Verifique se `disciplinas.txt` está na raiz do repositório.  
2. Execute:
   ```bash
   python3 create_structure.py
   ```
3. Aguarde:
   ```
   ✅ Estrutura de pastas criada com sucesso.
   ```
4. <!-- FUTURAMENTE: ![Passo Executar script](docs/images/run_script.png) -->

> **⚠️ Atenção:** **Sempre** execute `python3 create_structure.py` **antes** de adicionar, commitar e enviar suas alterações. Isso garante que a estrutura de pastas e o JSON/JS estejam atualizados.

### 5. Criar Pasta de Período Manualmente (Somente se Necessário)

> **Atenção:** somente pastas de período `<ANO>.<PERIODO>` podem ser criadas manualmente.

1. Dentro da pasta do professor, crie uma pasta com o período da prova.  
   Exemplo:
   ```
   decom/BCC501 - INTRODUCAO A CIENCIA DA COMPUTACAO/Saul Emanuel Delabrida Silva/25.1/
   ```

### 6. Adicionar a Fina

1. Copie o arquivo da prova para dentro da pasta de período criada.  
2. Renomeie o arquivo para:
   ```
   prova1.<extensão>
   ```
   Exemplos: `prova1.pdf`, `prova1.png`  
3. **Importante:** se o nome do arquivo ou o diretório de período não estiver no formato correto, seu Pull Request será **NEGADO**.

### 7. Commit e Push das Alterações

1. Verifique o status:
   ```bash
   git status
   ```
2. **⚠️ Não esqueça de rodar o script antes de commitar:**
   ```bash
   python3 create_structure.py
   ```
3. Adicione os arquivos:
   ```bash
   git add .
   ```
4. Crie um branch descritivo:
   ```bash
   git checkout -b adiciona-fina-BCC501-25.1
   ```
5. Faça o commit:
   ```bash
   git commit -m "Adiciona prova BCC501 25.1 para Saul Emanuel"
   ```
6. Envie para o **origin** (seu fork):
   ```bash
   git push origin adiciona-fina-BCC501-25.1
   ```

### 8. Abrir um Pull Request

1. No GitHub, acesse seu fork:  
   `https://github.com/<user>/finodromo.github.io`  
2. Clique em **Compare & pull request**.  
3. Compare:
   - **base**: `finodromo/finodromo.github.io:main`  
   - **compare**: `vodiniz/finodromo.github.io:first-commit` (ou seu branch)  
4. Preencha:
   - **Título** breve e descritivo.  
   - **Descrição** com o que foi adicionado.  
5. Clique em **Create pull request**.  
6. <!-- FUTURAMENTE: ![Passo Pull Request](docs/images/pull_request.png) -->

---

## 📌 Regras de Validação

- Disciplinas com código contendo `BCC` ➡️ `decom/`  
- Disciplinas com `MTM` ➡️ `demat/`  
- Demais ➡️ `outras/`  
- Pastas de disciplina e professor são geradas **automaticamente** pelo script.  
- **Somente** pastas de período `<ANO>.<PERIODO>` podem ser criadas manualmente.  
- Arquivos de prova devem se chamar `prova1.<extensão>`.  
  - Provas com mais de 1 página/foto devem estar no formato .pdf ou então devem estar dentro de uma pasta chamada provaX, e cada foto deve-se ser chamada de parte1.<extension>, parte2.<extension>...  
- Pull Requests que não seguirem o formato serão **NEGADOS**.

---

Pronto! Agora você já sabe como contribuir com o Finodromo. Boas contribuições! 🎉
