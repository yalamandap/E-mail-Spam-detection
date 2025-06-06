// Wait for DOM to load
document.addEventListener('DOMContentLoaded', () => {
  const clearBtn = document.getElementById('clearBtn');
  const textarea = document.getElementById('email_text');
  const resultBox = document.getElementById('resultBox');

  clearBtn.addEventListener('click', () => {
    textarea.value = '';
    if (resultBox) {
      resultBox.style.opacity = '0';
      setTimeout(() => resultBox.style.display = 'none', 600);
    }
    textarea.focus();
  });
});
