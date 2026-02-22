# Fontra — General Font Info Fields

A quick reference for the metadata fields found in the **General** panel of Fontra's Font Info section. These values are embedded inside the font file itself and are used by operating systems, applications, and font registries.

---

## Family name
The name of the font family — for example, *Garamond*, *Helvetica*, or your project name. This is what users see when browsing fonts in a word processor. All styles (Regular, Bold, Italic…) that belong together share the same family name.

## Copyright
A copyright notice for the typeface, typically in the form:
`Copyright © 2025 Your Name. All rights reserved.`
This is embedded in the font binary and helps establish legal authorship.

## Trademark
If the font name or design is trademarked, that notice goes here (e.g., *Helvetica is a trademark of Monotype GmbH.*). Most student projects will leave this empty.

## Description
A free-text field for a longer description of the font — its intended use, design concept, historical references, etc. Some applications display this to end users.

## Sample text
A custom string that font browsers can display as a preview instead of the default "Aa" or pangram. Useful if your font has a specific character set or personality you want to showcase.

## Designer
The name of the person (or people) who designed the typeface. This is you — or your team.

## Designer URL
A web address associated with the designer, usually a portfolio or studio website (e.g., `https://yourportfolio.com`).

## Manufacturer
The name of the foundry or organisation that produced and distributes the font. For student work this is often the same as the designer, or your school/programme name.

## Manufacturer URL
The website of the manufacturer/foundry.

## License description
A plain-language description of the terms under which the font may be used. For example:
*This font is released under the SIL Open Font License, Version 1.1.*
Commercial fonts may say something like *For use on up to 5 devices. No embedding permitted.*

## License info URL
A link to the full licence document — for instance, `https://openfontlicense.org` for OFL fonts.

## Vendor ID
A four-character code that uniquely identifies the font vendor in the OpenType specification (e.g., `ADBE` for Adobe). Registered vendors have codes assigned by Microsoft. For personal or student projects this is often left blank or set to a custom four-letter tag.

## Version Major
The whole-number part of the font version (e.g., `1` in version 1.2). Increment this for significant, breaking releases.

## Version Minor
The decimal part of the version number (e.g., `2` in version 1.2). Increment this for smaller updates and bug fixes.

## Units Per Em (UPM)
The number of design units that fit in one em — the fundamental coordinate grid of the font. **1000** is standard for PostScript/OpenType fonts; 2048 is common for TrueType. All your glyph drawings are scaled relative to this value. Changing it after you've started drawing will rescale everything, so set it early and leave it.

---

*Reference: OpenType Specification — [Name table](https://learn.microsoft.com/en-us/typography/opentype/spec/name) and [OS/2 table](https://learn.microsoft.com/en-us/typography/opentype/spec/os2).*
