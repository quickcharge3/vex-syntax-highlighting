A grammar and theme file for Houdini's Vector Expressions (vex) language for use with Obsidian.

# Usage

Install and enable Shiki Highlighter Community Plugin for Obsidian

https://github.com/mProjectsCode/obsidian-shiki-plugin

Create two folders anywhere within your vault, for example

```
/YourVault/ShikiGrammar/
/YourVault/ShikiThemes/
```

Paste the grammar file `(/syntaxes/vex.tmLanguage.json)` and theme file `(/themes/vex.tmTheme.json)` into their respective folders, open the Shiki plugin settings and point the plugin towards these folders via the plugin settings

When creating a new codeblock or inline code, use "vex" as the language identifier for the code block

______________

![alt text](image-2.png)

![alt text](image-1.png)