// Global CSRF helper (add CSRF token to fetch requests if WTF is enabled)
function csrfHeaders() {
    const meta = document.querySelector('meta[name="csrf-token"]');
    return meta ? {'X-CSRFToken': meta.content, 'Content-Type': 'application/json'} : {'Content-Type': 'application/json'};
}

// Auto-dismiss flash alerts after 4 seconds
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.alert.alert-dismissible').forEach(el => {
        setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(el);
            bsAlert.close();
        }, 4000);
    });
});
