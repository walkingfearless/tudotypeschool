# Primeiros Passos com o Fontra

O Fontra é um editor de tipos gratuito, open-source e baseado em browser, construído de raiz para fontes variáveis. Desenvolvido pela Black[Foundry] e Just van Rossum com apoio do Google Fonts, nasceu para o design e produção de grandes conjuntos de caracteres CJK, mas cresceu até se tornar um editor quase completo, adequado a qualquer projecto tipográfico.

Por correr no browser, o Fontra funciona em macOS, Windows e Linux com a mesma interface. Podes editar ficheiros locais através da aplicação complementar **Fontra Pak**, ou ligar a um servidor remoto para colaboração em tempo real com outros designers.

---

## 1 — Instalar o Fontra Pak

O Fontra Pak é uma aplicação autónoma que inicia um servidor Fontra local e abre o editor no teu browser predefinido.

| Plataforma | Como instalar |
|---|---|
| **macOS** | Descarrega o `.dmg` de [fontra.xyz](https://fontra.xyz/), abre o pacote e arrasta o Fontra Pak para a pasta Aplicações. |
| **Windows 10/11** | Descarrega o `.zip` de [fontra.xyz](https://fontra.xyz/), extrai-o e faz duplo clique no instalador. |
| **Linux (Ubuntu)** | Pesquisa *fontrapak* no Ubuntu Software, ou instala o snap: `sudo snap install fontrapak`. O Flatpak também está disponível. |

> Para instruções detalhadas por plataforma, consulta a [documentação de instalação](https://docs.fontra.xyz/how-tos/installation/installing-fontra-pak/).

---

## 2 — Abrir uma Fonte

1. Faz duplo clique no ícone do **Fontra Pak** — aparece uma pequena janela de arranque.
2. **Arrasta** um ficheiro `.ufo`, `.designspace`, `.fontra`, `.glyphs` ou `.glyphspackage` para essa janela.
3. O Fontra abre no browser. Aterras na **Vista Geral da Fonte** — uma grelha com todos os glifos da fonte.
4. **Faz duplo clique** em qualquer célula de glifo para entrar na **Vista de Edição** e começar a desenhar.

Também podes abrir ficheiros `.ttf` ou `.otf` compilados apenas para inspecção (só de leitura).

---

## 3 — Formatos de Ficheiro Suportados

| Formato | Leitura | Escrita |
|---|---|---|
| `.fontra` | Sim | Sim |
| `.ufo` / `.designspace` | Sim | Sim |
| `.glyphs` / `.glyphspackage` | Sim | Sim (parcial — via plugin) |
| `.ttf` / `.otf` | Sim | — |
| `.rcjk` (RoboCJK) | Sim (via plugin) | Sim (via plugin) |

---

## 4 — Funcionalidades Principais

### Design variável em primeiro lugar
Cada glifo pode ter as suas próprias fontes em qualquer localização no espaço de design. Os eixos de variação não têm de ser globais — podes definir eixos locais ao glifo e usar **componentes variáveis** (semelhantes aos Smart Components do Glyphs) para construir formas modulares e paramétricas.

### Baseado em browser, multiplataforma
O cliente é escrito em JavaScript e corre em qualquer browser moderno; o servidor é Python. Por ser baseado em browser, a interface é idêntica em macOS, Windows e Linux.

### Colaboração em tempo real
Quando o Fontra corre num servidor partilhado, vários designers podem editar a mesma fonte em simultâneo — cada um a trabalhar em glifos diferentes, sem conflitos. Este era um requisito central para equipas de produção CJK de grande dimensão.

### Camadas de fundo e imagens
Podes criar camadas de fonte adicionais por glifo para esboços, variações ou formas de referência. Imagens de fundo (PNG ou JPEG) podem ser colocadas dentro de um glifo com opacidade ajustável, e são maioritariamente compatíveis com o formato de imagem de fundo UFO.

### Edição de features OpenType
Um painel de código integrado (baseado no CodeMirror) permite-te criar e editar código-fonte de features OpenType directamente no Fontra, sem precisar de mudar para um editor de texto externo.

### Kerning
A ferramenta de Kerning coexiste com a nova ferramenta de Sidebearing. Selecciona um par de glifos e arrasta ou usa as teclas de seta para ajustar valores. As teclas modificadoras limitam as edições a incrementos de 5, 10 ou 50 unidades. Um menu de contexto permite criar excepções de kerning para pares de grupos.

### Informação da Fonte e tabelas de baixo nível
O painel de Informação da Fonte expõe metadados (nome da família, versão, UPM, etc.) bem como definições de tabelas OpenType de baixo nível (hhea, vhea, OS/2), para um controlo fino do resultado binário.

### Suporte a grandes conjuntos de caracteres
O Fontra foi concebido desde o início para lidar com fontes com dezenas de milhares de glifos — a navegação, pesquisa e edição mantêm-se fluidas mesmo em projectos CJK massivos.

---

## 5 — A Interface em Resumo

O Fontra tem duas vistas principais:

**Vista Geral da Fonte** — uma grelha com todos os glifos. Podes filtrar por conjuntos de glifos (colecções predefinidas independentes da fonte), pesquisar por nome ou Unicode, e ver células marcadoras de posição para caracteres ainda não desenhados.

**Vista de Edição** — onde se desenha e edita. A barra de ferramentas à esquerda dá acesso às ferramentas de desenho e edição. Os painéis à direita fornecem contexto: navegação no espaço de design, informação do glifo, transformações, fontes de referência, texto de pré-visualização, e muito mais.

---

## 6 — Ferramentas de Desenho e Edição

| Ferramenta | Função |
|---|---|
| **Ponteiro** | Seleccionar, mover e transformar pontos e contornos. |
| **Caneta** | Desenhar novos contornos de Bézier. Uma sub-ferramenta muda para curvas quadráticas. |
| **Faca** | Cortar contornos. |
| **Forma** | Desenhar formas geométricas básicas (rectângulos, elipses). |
| **Régua** | Medir distâncias e ângulos. |
| **Mão** | Mover o canvas. |
| **Sidebearing** | Ajustar os espaços laterais esquerdo e direito visualmente. Mantém Alt premido para mover os espaços opostos simetricamente. |
| **Kerning** | Ajustar o kerning de par por arrasto ou com as teclas de seta. Shift+clique para multi-seleccionar pares. |

---

## 7 — Referência Rápida

### Navegação

| Acção | Atalho / Gesto |
|---|---|
| Mover o canvas | Ferramenta Mão **ou** Espaço + arrastar |
| Zoom in / out | Roda do rato ou gesto de pinça |
| Glifo anterior / seguinte | Setas (configurável) |
| Abrir glifo da Vista Geral | Duplo clique na célula do glifo |
| Regressar à Vista Geral da Fonte | Fechar o separador do editor ou usar o menu |

### Edição essencial

| Acção | Como |
|---|---|
| Mudar para a ferramenta Caneta | Seleccionar na barra de ferramentas (atalho personalizado disponível) |
| Alternar cúbico / quadrático | Usar o selector de sub-ferramenta da Caneta |
| Desfazer / Refazer | Cmd/Ctrl + Z / Shift + Cmd/Ctrl + Z (por glifo) |
| Limitar kerning a 10 unidades | Manter tecla modificadora enquanto arrastas |
| Criar excepção de kerning | Clique direito com a ferramenta Kerning activa |
| Adicionar camada de fundo | Painel de Camadas — adicionar nova camada de fonte ao glifo actual |
| Colocar imagem de fundo | Arrastar PNG/JPEG para o glifo, ou usar o painel de imagem |

### Formatos em resumo

| Quero… | Usar este formato |
|---|---|
| Edição nativa sem perdas | `.fontra` |
| Interoperabilidade com outros editores | `.ufo` / `.designspace` |
| Abrir um ficheiro Glyphs directamente | `.glyphs` / `.glyphspackage` |
| Inspecionar uma fonte compilada | `.ttf` / `.otf` (só de leitura) |

### Links úteis

| Recurso | URL |
|---|---|
| Fontra (início) | [fontra.xyz](https://fontra.xyz/) |
| Documentação | [docs.fontra.xyz](https://docs.fontra.xyz/) |
| Blog / actualizações | [blog.fontra.xyz](https://blog.fontra.xyz/) |
| Changelog | [fontra.xyz/changelog.html](https://fontra.xyz/changelog.html) |
| GitHub | [github.com/fontra](https://github.com/fontra) |

---

*Fontes: [Documentação Fontra](https://docs.fontra.xyz/), [Blog Fontra](https://blog.fontra.xyz/), [GitHub Fontra](https://github.com/fontra/fontra).*
