---
trigger: manual
---

# Style Guide for Notes

This document outlines the style conventions for markdown notes to ensuring consistency and professional formatting.

## Callouts (Obsidian Style)

Use callouts to highlight definitions, theorems, and examples.

### Definitions
Use the `INFO` callout type.
```markdown
> [!INFO] Definition: Term
> Definition text here.
```

### Theorems and Lemmas
Use the `TIP` callout type.
```markdown
> [!TIP] Theorem: Name (Optional)
> Statement of the theorem.
```

### Proofs
Use the `NOTE` callout type. If distinct from the theorem, consider making it collapsible (`-`).
```markdown
> [!NOTE]- Proof
> Step-by-step derivation.
```

### Examples
Use the `EXAMPLE` callout type.
```markdown
> [!EXAMPLE] Title
> Example details.
```

### Questions/Exercises
Use `QUESTION` or specific custom callouts if available (`c` for custom color if configured).
```markdown
> [!QUESTION]
> Question text?
```

## Structure

- **Title**: The file should start with frontmatter followed by an H1 title.
- **Headers**:
  - H2 (`##`) for main sections.
  - H3 (`###`) for subsections.
  - Avoid using H4 unless absolutely necessary deep nesting is required.

## Mathematical Notation (LaTeX)

- **Vectors**: Use `\vec{v}` (e.g., $\vec{v}$) rather than `\mathbf{v}` or `\boldsymbol{v}`.
- **Norms**: Use `\lVert \vec{x} \rVert` for norms.
- **Inner Products**: Use `\langle \vec{x}, \vec{y} \rangle`.
- **Number Sets**: Use `\mathbb{R}`, `\mathbb{N}`, etc.
- **Text in Math**: Use `\text{...}` for non-math text within equations.
- **Display Math**: Use `$$ ... $$` on new lines.

## Diagrams

- Use **TikZ** within markdown code blocks for diagrams.
- Format:
  ```markdown
  ```tikz
  \begin{document}
  \begin{tikzpicture}
      ...
  \end{tikzpicture}
  \end{document}
  ```
  ```
