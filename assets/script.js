window.MathJax = {
  tex: { inlineMath: [['$', '$'], ['$$', '$$']] },
  svg: { fontCache: 'global' }
};
document.addEventListener('DOMContentLoaded', () => {
  hljs.highlightAll();
  document
    .querySelectorAll('pre code.language-mermaid')
    .forEach((codeMermaid) => {
      const div = document.createElement('div');
      div.classList.add('mermaid');
      div.textContent = codeMermaid.textContent;
      codeMermaid.parentElement.replaceWith(div);
    });
  const script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js';
  script.onload = () => mermaid.initialize({ startOnLoad: true });
  document.head.appendChild(script);
});
