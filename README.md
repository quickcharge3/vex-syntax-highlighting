a grammar and theme file for Houdini's Vector Expressions (vex) language for use with Obsidian.

Usage

Install Shiki Highlighter Community Plugin for Obsidian

Create two folders anywhere within your vault

/YourVault/ShikiGrammar/
/YourVault/ShikiThemes/

paste the grammar and theme file into their respective folders and point the Shiki plugin towards them

when creating a new codeblock or inline code, use "vex" as the language identifier

``` \vex

string foo = "Hello World";

```