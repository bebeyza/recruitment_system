// Silme onayı
function confirmDelete(event, itemName) {
    if (!confirm(itemName + ' silmek istediğinize emin misiniz?')) {
        event.preventDefault();
        return false;
    }
    return true;
}

// Form validasyonu
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
            let isValid = true;

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = '#e53e3e';
                } else {
                    input.style.borderColor = '#e2e8f0';
                }
            });

            if (!isValid) {
                e.preventDefault();
                alert('Lütfen tüm zorunlu alanları doldurun.');
            }
        });
    });

    // Sayfa yüklendiğinde animasyon
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'all 0.5s ease';

            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, 50);
        }, index * 100);
    });
});

// Arama fonksiyonu (opsiyonel)
function searchTable() {
    const input = document.getElementById('searchInput');
    if (!input) return;

    const filter = input.value.toLowerCase();
    const table = document.querySelector('table');
    const rows = table.querySelectorAll('tbody tr');

    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(filter) ? '' : 'none';
    });
}