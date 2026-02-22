# Configurar o GitHub

Um guia passo a passo para os alunos do workshop — desde a criação de uma conta até à entrega do primeiro projecto.

---

## O que é o GitHub?

O GitHub é uma plataforma para guardar e partilhar ficheiros através do **Git**, um sistema de controlo de versões. Neste workshop usamo-lo para distribuir materiais de aula e recolher os projectos dos alunos. Pensa nele como uma pasta partilhada que guarda o histórico completo de todas as alterações que fizeres.

---

## Passo 1 — Criar uma Conta no GitHub

1. Acede a [github.com](https://github.com) e clica em **Sign up**
2. Escolhe um nome de utilizador, introduz o teu endereço de email e uma palavra-passe
3. Verifica o teu email quando solicitado
4. O plano gratuito é suficiente — não subscrevas nenhuma modalidade paga

**Dica para o nome de utilizador:** usa algo profissional e reconhecível, como `nome-apelido` ou `napelido`. Vai fazer parte do URL do teu perfil público.

---

## Passo 2 — Instalar o GitHub Desktop

O GitHub Desktop é uma aplicação visual que te permite gerir o teu trabalho sem usar a linha de comandos.

1. Faz o download em [desktop.github.com](https://desktop.github.com)
2. Instala e abre a aplicação
3. Inicia sessão com a tua conta do GitHub quando solicitado

---

## Passo 3 — Clonar o Repositório do Workshop

Clonar cria uma cópia local do repositório no teu computador.

1. No GitHub Desktop, vai a **File → Clone Repository**
2. Clica no separador **URL**
3. Cola o URL do repositório fornecido pelo docente
4. Escolhe onde guardar a pasta no teu computador (por exemplo: `Documentos/UAlg-TypeWorkshop`)
5. Clica em **Clone**

Passas a ter uma cópia completa de todos os materiais do workshop no teu computador.

---

## Passo 4 — Preparar a Tua Pasta de Projecto

Todos os projectos dos alunos ficam dentro de `02-UAlg-Type-Workshop/03_PROJECTS/`. É disponibilizada uma pasta modelo para copiares.

1. Abre a pasta `03_PROJECTS/` no teu computador
2. Encontra a pasta chamada `_TEMPLATE`
3. Duplica-a (copia e cola — não moves nem renomeias o original)
4. Renomeia a tua cópia com o formato `nome-apelido` — por exemplo: `ana-silva`
5. Abre o ficheiro `README.md` dentro da tua pasta e preenche o teu nome, o nome do projecto e uma breve descrição do que pretendes desenhar

A tua pasta contém quatro subpastas:

| Pasta | O que vai aqui |
|---|---|
| `sources/` | Ficheiros de trabalho — Fontra, UFO, Glyphs |
| `exports/` | Fontes compiladas — TTF, OTF, variável |
| `proofs/` | Espécimes em PDF, provas de impressão |
| `references/` | Esboços, digitalizações, imagens de referência |

---

## Passo 5 — Fazer Commit e Push do Teu Trabalho

O commit guarda um instantâneo das tuas alterações. O push envia-as para o GitHub.

1. Abre o GitHub Desktop — os ficheiros alterados aparecem listados à esquerda
2. Escreve uma descrição curta no campo **Summary** — por exemplo: `Adicionar primeiros desenhos de H e O`
3. Clica em **Commit to main**
4. Clica em **Push origin** (canto superior direito) para carregar as alterações para o GitHub

Repete este processo sempre que fizeres progressos significativos. Trata os commits como pontos de gravação.

---

## Regras de Ficheiros

**Permitido — podes fazer commit livremente:**

- Ficheiros de fonte: `.fontra`, `.ufo`, `.glyphs`, `.designspace`
- Fontes compiladas: `.ttf`, `.otf`
- Espécimes e provas: `.pdf`
- Imagens de referência: `.jpg`, `.png`, `.svg`

**Não permitido — não faças commit destes ficheiros:**

- Ficheiros fonte Adobe: `.ai`, `.psd`, `.indd` — podem ocupar centenas de megabytes
- Vídeos: `.mp4`, `.mov`, `.avi`
- Arquivos comprimidos: `.zip`, `.rar`
- Qualquer ficheiro individual com mais de 50 MB

Em caso de dúvida, pergunta ao docente antes de fazer commit.

---

## Dicas Úteis

- **Faz pull antes de trabalhar:** antes de começar uma sessão, clica em **Fetch origin** no GitHub Desktop para descarregar as actualizações do docente
- **Faz commit com frequência:** commits pequenos e regulares são muito mais fáceis de rever do que um único carregamento no final do semestre
- **Escreve descrições claras:** `Teste ao eixo de peso` é mais útil do que `actualização` ou `alterações`
