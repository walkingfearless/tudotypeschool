# Fontra — Campos de Informação Geral da Fonte

Referência rápida para os campos de metadados do painel **General** (Geral) do Font Info no Fontra. Estes valores são guardados dentro do próprio ficheiro de fonte e são utilizados pelo sistema operativo, pelas aplicações e pelos registos de tipos de letra.

---

## Family name — Nome da família
O nome da família tipográfica — por exemplo, *Garamond*, *Helvetica*, ou o nome do teu projecto. É o que os utilizadores vêem ao navegar pelas fontes num processador de texto. Todos os estilos (Regular, Bold, Italic…) que pertencem ao mesmo conjunto partilham o mesmo nome de família.

## Copyright — Direitos de autor
Um aviso de direitos de autor para o tipo de letra, normalmente com a forma:
`Copyright © 2025 O Teu Nome. Todos os direitos reservados.`
Este campo fica gravado no ficheiro binário da fonte e ajuda a estabelecer a autoria legal.

## Trademark — Marca registada
Se o nome ou o design da fonte estiver registado como marca, o respectivo aviso vai aqui (ex.: *Helvetica é uma marca registada da Monotype GmbH.*). A maioria dos projectos académicos deixa este campo vazio.

## Description — Descrição
Um campo de texto livre para uma descrição mais extensa da fonte — o seu uso previsto, conceito de design, referências históricas, etc. Algumas aplicações mostram este texto ao utilizador final.

## Sample text — Texto de exemplo
Uma sequência de texto personalizada que os navegadores de fontes podem mostrar como pré-visualização, em vez do habitual "Aa" ou de um pangrama. Útil quando a tua fonte tem um conjunto de caracteres específico ou uma personalidade que queres destacar.

## Designer — Designer
O nome da pessoa (ou das pessoas) que desenhou o tipo de letra. És tu — ou a tua equipa.

## Designer URL — URL do designer
Um endereço web associado ao designer, normalmente um portfólio ou sítio de estúdio (ex.: `https://o-teu-portfolio.com`).

## Manufacturer — Fabricante
O nome da fundição ou organização que produziu e distribui a fonte. Em trabalhos académicos, é muitas vezes o mesmo que o designer, ou o nome da escola/curso.

## Manufacturer URL — URL do fabricante
O sítio web da fundição ou fabricante.

## License description — Descrição da licença
Uma descrição em linguagem corrente das condições em que a fonte pode ser utilizada. Por exemplo:
*Esta fonte é disponibilizada sob a SIL Open Font License, Versão 1.1.*
As fontes comerciais podem indicar algo como: *Para uso em até 5 dispositivos. Não é permitida a incorporação em documentos.*

## License info URL — URL da informação de licença
Uma ligação para o documento completo da licença — por exemplo, `https://openfontlicense.org` para fontes OFL.

## Vendor ID — Identificador do fornecedor
Um código de quatro caracteres que identifica de forma única o fornecedor da fonte na especificação OpenType (ex.: `ADBE` para a Adobe). Os fornecedores registados têm códigos atribuídos pela Microsoft. Para projectos pessoais ou académicos, este campo é frequentemente deixado em branco ou preenchido com uma etiqueta de quatro letras à escolha.

## Version Major — Versão principal
A parte inteira do número de versão da fonte (ex.: `1` na versão 1.2). Deve ser incrementada em lançamentos significativos que introduzam alterações profundas.

## Version Minor — Versão secundária
A parte decimal do número de versão (ex.: `2` na versão 1.2). Deve ser incrementada em actualizações menores e correcções de erros.

## Units Per Em — Unidades por Em (UPM)
O número de unidades de design que cabem num em — a grelha de coordenadas fundamental da fonte. **1000** é o valor padrão para fontes PostScript/OpenType; 2048 é comum em TrueType. Todos os teus desenhos de glifos são escalados em relação a este valor. Alterar o UPM depois de teres começado a desenhar irá redimensionar tudo, por isso define-o no início e não o alteres.

---

*Referência: Especificação OpenType — [tabela Name](https://learn.microsoft.com/en-us/typography/opentype/spec/name) e [tabela OS/2](https://learn.microsoft.com/en-us/typography/opentype/spec/os2).*
