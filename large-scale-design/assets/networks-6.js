function highlightTriangle() {
  const triangle = document.querySelector('.triangle');
  triangle.style.transform = 'scale(1.1)';
  triangle.style.transition = 'transform 0.3s ease';
  setTimeout(() => {
      triangle.style.transform = 'scale(1)';
  }, 300);
}

document.querySelectorAll('.property').forEach(property => {
  property.addEventListener('click', function(e) {
    e.stopPropagation();
    document.querySelectorAll('.property').forEach(p => {
      p.style.background = 'white';
      p.style.transform = 'translateY(0)';
    });
    this.style.background = 'rgba(255, 255, 255, 0.9)';
    this.style.transform = 'translateY(-10px)';
    setTimeout(() => {
      this.style.background = 'white';
      this.style.transform = 'translateY(0)';
    }, 2000);
  });
});
document.querySelectorAll('.combination').forEach(combo => {
  combo.addEventListener('mouseenter', function() {
    this.style.transform = 'translateY(-8px) scale(1.02)';
  });
  combo.addEventListener('mouseleave', function() {
    this.style.transform = 'translateY(0) scale(1)';
  });
});
