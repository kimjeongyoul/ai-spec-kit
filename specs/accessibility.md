# ♿ Web Accessibility Specification (WCAG 2.1)

Ensuring all users, including those with disabilities, can access and use this project.

## 1. Semantic HTML
- Use proper elements: `<main>`, `<nav>`, `<header>`, `<footer>`, `<section>`.
- Use heading levels (`<h1>`-`<h6>`) in correct sequential order.

## 2. Visual & Interaction
- **Alt Text**: All images must have meaningful alternative text.
- **Keyboard Navigation**: All interactive elements must be accessible via keyboard.
- **Color Contrast**: Maintain a minimum contrast ratio of 4.5:1 for text.

## 3. ARIA (Accessible Rich Internet Applications)
- Use WAI-ARIA roles and attributes only when native HTML is insufficient.
- Ensure `aria-label` or `aria-labelledby` is used for non-text interactive elements.
