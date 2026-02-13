---
trigger: manual
description: Style guide for creating notes, based on Optimization.md and Templates.
---

# Style Guide for Notes

This guide outlines the formatting and structural conventions for creating notes, based on existing class notes (e.g., `Optimization.md`) and templates.

## 1. Frontmatter

All notes should begin with the following YAML frontmatter:

```yaml
---
publish: true
---
```

## 2. Headings & Structure

*   **Title**: Use a single H1 (`#`) for the document title.
*   **Sections**: Use H2 (`##`) for major sections.
*   **Subsections**: Use H3 (`###`) and H4 (`####`) for nested content.
*   **Lists**: Use numbered lists for sequential items and bullet points for unordered lists.

## 3. Callouts (Obsidian/GitHub Style)

Use specific callout types for mathematical definitions, theorems, and proofs.

### Definitions
Use the `INFO` callout.
```markdown
> [!INFO] Definition: Term Name
> Definition text goes here...
```

### Theorems, Lemmas, Corollaries
Use the `TIP` callout.
```markdown
> [!TIP] Theorem: Theorem Name
> Theorem statement...
```
*(Also applies to Lemmas and Corollaries)*

### Proofs
Use the `NOTE` callout, commonly collapsed (`-`).
```markdown
> [!NOTE]- Proof
> Proof steps go here...
> $\blacksquare$
```

### Examples
Use the `EXAMPLE` callout.
```markdown
> [!EXAMPLE] Example Title
> Example details...
```

### Exercises / Questions
Use the `QUESTION` callout (or `c` if specifically requested, but `QUESTION` is the template standard).
```markdown
> [!QUESTION] Exercise
> Exercise text...
```

## 4. Mathematics (LaTeX)

*   **Inline Math**: Use single dollar signs, e.g., `$f(x) = x^2$`.
*   **Block Math**: Use double dollar signs, e.g., `$$ f(x) = \int x dx $$`.
*   **Environments**:
    *   Use `pmatrix` for matrices.
    *   Use `align*` or `gather` for multi-line equations inside `$$` blocks.
*   **Notation**:
    *   Vectors: `\vec{x}`
    *   Inner Products: `\langle \vec{x}, \vec{y} \rangle`
    *   Sets: `\mathbb{R}^n`, `\mathcal{P}`
*   **Package Check**: **ALWAYS** check if symbols require `amsmath`, `amssymb`, or other packages. Ensure these are assumed or included if the environment requires (though Obsidian usually handles standard LaTeX).

## 5. Figures (TikZ)

When generating TikZ figures, strictly follow these rules:

1.  **Wrapper**:
    ```latex
    \begin{document}
    \begin{tikzpicture}[>=stealth, scale=1]
      % TikZ code
    \end{tikzpicture}
    \end{document}
    ```
2.  **Scale**: **ALWAYS** keep `scale` at **1.0 or below**. Never use a scale > 1.0.
3.  **Colors**:
    *   Do **NOT** use similar colors for filling shapes and for the text overlaying them. Ensure high contrast.
    *   Standard fill: `blue!10`, `green!20`, `gray!10`.
    *   Standard draw/text: `blue!80!black`, `red!70!black`, `black`.

## 6. General Formatting

*   **Bold**: Use `**text**` for emphasis on defined terms or key concepts.
*   **Italics**: Use `*text*` sparingly for emphasis.
*   **Links**: Use `[[wikilinks]]` for internal references.
*   **Images**: Use `![[image.png]]` for embeddings.