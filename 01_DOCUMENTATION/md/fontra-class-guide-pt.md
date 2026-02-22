# Fontra Pak — Guia de Aula

> **Antes deste guia:** instala o Fontra Pak e lê a visão geral da interface em [**Fontra — Primeiros Passos**](fontra-getting-started-pt.html). Este documento pressupõe que o Fontra Pak já está a correr no teu computador.

---

## 1 — Abrir o Projecto de Fonte Variável da Aula

### Sobre a ZalandoSans

A fonte de demonstração da aula é **ZalandoSans-VariableFont.fontra**, localizada na pasta `02_DEMO` da unidade da aula. Trata-se da tipografia open-source [Zalando Sans](https://github.com/zalando/sans), lançada pela Zalando SE sob a Licença de Tipos Abertos SIL — um sans-serif contemporâneo com dois eixos variáveis:

| Eixo | Tag | Intervalo | Predefinição |
|---|---|---|---|
| Peso | `wght` | 200 – 900 | 400 (Regular) |
| Largura | `wdth` | 75 – 125 | 100 (Normal) |

### Abrir o ficheiro

1. Inicia o **Fontra Pak** — aparece a janela de arranque.
2. No Finder / Explorador de Ficheiros, navega até `02_DEMO/` na unidade da aula.
3. **Arrasta `ZalandoSans-VariableFont.fontra` para a janela de arranque do Fontra Pak**.
4. O browser abre automaticamente e aterra na **Vista Geral da Fonte** — uma grelha com todos os glifos da fonte.

### Explorar os eixos variáveis

1. Faz duplo clique em qualquer glifo — experimenta com **H**, **O** ou **n** — para entrar na **Vista de Edição**.
2. No painel do lado direito, abre o painel **Espaço de Design** (ícone de bússola).
3. Arrasta os cursores de **Peso** e **Largura** — o glifo actualiza em tempo real.
4. Clica em qualquer posição no mapa de eixos 2-D para saltar directamente para essa localização.

### Usar a ZalandoSans como Fonte de Referência durante o teu trabalho

1. Abre o teu próprio projecto numa sessão do Fontra Pak.
2. No painel direito, abre o painel **Fontes de Referência**.
3. Clica em **+** e navega até `ZalandoSans-VariableFont.fontra`.
4. O glifo de referência aparece em cinzento por baixo dos teus desenhos — usa-o para comparar proporções, não para decalcar.

---

## 2 — Iniciar um Novo Projecto do Zero

### Criar o ficheiro de fonte

1. Na janela de arranque do Fontra Pak, clica em **New Font…**
2. Uma fonte nova e vazia abre no browser.
3. Quando solicitado, escolhe um local de gravação dentro da pasta do teu projecto e dá um nome ao ficheiro (ex.: `MinhaFamilia.fontra`).
   O Fontra guarda automaticamente a partir deste momento — não há passo manual de *Guardar*.

### Configurar a Informação da Fonte

Abre o painel **Informação da Fonte** (ícone ⓘ na barra de ferramentas superior) e preenche no mínimo:

| Campo | Valor recomendado |
|---|---|
| Nome da Família | O nome da tua tipografia |
| Unidades Por Em (UPM) | `1000` (padrão PostScript) |
| Ascendente | `800` |
| Altura de Caixa Alta | `700` |
| Altura-x | `500` |
| Descendente | `-200` |

### Adicionar um eixo variável (opcional — apenas para fontes variáveis)

1. Na Informação da Fonte, desce até à secção **Eixos** e clica em **+**.
2. Eixo de partida padrão: `wght` Peso — mín. `100`, predefinição `400`, máx. `900`.
3. Clica em **Add source** para colocar masters — ex.: Regular em 400, Bold em 700.
4. O Fontra cria camadas de fonte separadas para cada localização de master.

> Para um primeiro projecto na aula, **trabalha com um único master**. Só adiciona um segundo quando o primeiro estiver sólido.

### Desenhar os primeiros glifos

Segue a ordem de desenho estabelecida nas aulas de tipografia:

- **Caixa Alta:** `H` e depois `O` — todos os outros caracteres maiúsculos derivam destas proporções.
- **Caixa Baixa:** `n`, depois `o`, depois `y` — juntos definem o arco, a contraforma oval e a descendente.

Para adicionar um glifo:

1. Na Vista Geral da Fonte, clica em **+** (ou clique direito numa célula vazia → **Add glyph**).
2. Escreve o nome do glifo (ex.: `H`) — o Fontra preenche o valor Unicode automaticamente para caracteres padrão.
3. Faz duplo clique na nova célula para abrir a **Vista de Edição** e começar a desenhar.

### Importar um esboço digitalizado como fundo

1. Na Vista de Edição, abre o painel **Camadas** no lado direito.
2. Clica em **+** e dá um nome à nova camada (ex.: `esboço`).
3. Arrasta um PNG ou JPEG digitalizado para o canvas do glifo — fica na camada activa.
4. Reduz a opacidade nas definições da camada para que não concorra com os teus contornos.

---

## 3 — Exportar Ficheiros de Fonte

### Gravação automática nativa — .fontra (sempre activa)

A tua pasta `.fontra` no disco está sempre actualizada. Não é necessário exportar para continuar o trabalho.

### Exportar para UFO + DesignSpace

O formato de intercâmbio padrão — compatível com RoboFont, Glyphs e o pipeline de build do Google Fonts.

1. **Ficheiro → Exportar como…**
2. Escolhe **UFO + DesignSpace**.
3. Selecciona um destino **fora** da pasta da tua fonte `.fontra`.
4. Clica em **Exportar** — o Fontra escreve um `.ufo` por master mais um ficheiro `.designspace`.

### Exportar para TTF / OTF Variável

Para produzir uma fonte binária para testar em aplicações ou browsers:

1. **Ficheiro → Exportar como…** → **Variable TTF** (ou Variable OTF).
2. Escolhe um destino e clica em **Exportar** — o Fontra compila a fonte directamente, sem ferramentas externas.

### Exportar instâncias estáticas

Para produzir ficheiros de estilos individuais (Regular.ttf, Bold.ttf, etc.):

1. **Ficheiro → Exportar como…** → **Static TTF instances**.
2. O Fontra gera um binário por localização de master definida.

> **Prova rápida:** instala o `.ttf` exportado no sistema, ou arrasta-o para [wakamaifondue.com](https://wakamaifondue.com) para inspeccionar todos os eixos variáveis e features OpenType directamente no browser.

---

## Links Úteis

| Recurso | URL |
|---|---|
| Fontra — Primeiros Passos (geral) | [fontra-getting-started-pt.html](fontra-getting-started-pt.html) |
| Documentação Fontra | [docs.fontra.xyz](https://docs.fontra.xyz/) |
| Zalando Sans (referência open-source) | [github.com/zalando/sans](https://github.com/zalando/sans) |
| Prova de fontes | [wakamaifondue.com](https://wakamaifondue.com) |

---

*Fontes: [Fontra Docs – Export as](https://docs.fontra.xyz/reference/menu/file/export-as) · [Zalando Sans](https://github.com/zalando/sans)*
