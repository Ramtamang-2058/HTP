// Light / dark theme toggle
(function () {
    const html = document.documentElement;
    const saved = localStorage.getItem('htp-theme') || 'dark';
    html.setAttribute('data-theme', saved);

    function applyIcon(theme) {
        const icon = document.getElementById('themeIcon');
        if (icon) icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    }

    applyIcon(saved);

    document.getElementById('themeToggle')?.addEventListener('click', () => {
        const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', next);
        localStorage.setItem('htp-theme', next);
        applyIcon(next);
    });
})();

// Navbar scroll
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
});

// Mobile nav
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');
const closeNav = document.getElementById('closeNav');

hamburger.addEventListener('click', () => mobileNav.classList.add('open'));
closeNav.addEventListener('click', () => mobileNav.classList.remove('open'));
document.querySelectorAll('.mobile-nav a').forEach(a => {
    a.addEventListener('click', () => mobileNav.classList.remove('open'));
});

// Typewriter
const phrases = [
    "Leading Nepal's Tech Evolution",
    "नेपाली प्रविधिको नेतृत्व गर्दै",
    "Connecting Nepal to the Cosmos",
    "Building Tomorrow's Robots Today",
    "Pioneering AI Innovation in Nepal",
    "Nepal's First Supercomputer Builders"
];
let pi = 0, ci = 0, deleting = false;
const tw = document.getElementById('typewriter');

function type() {
    if (!tw) return;
    const phrase = phrases[pi % phrases.length];
    tw.textContent = phrase.slice(0, ci);
    if (!deleting && ci < phrase.length) {
        ci++;
        setTimeout(type, 72);
    } else if (deleting && ci > 0) {
        ci--;
        setTimeout(type, 38);
    } else {
        deleting = !deleting;
        if (!deleting) pi++;
        setTimeout(type, deleting ? 80 : 1600);
    }
}
type();

// Hero parallax on scroll
window.addEventListener('scroll', () => {
    const bg = document.querySelector('.hero-bg');
    if (bg) bg.style.transform = `scale(1.08) translateY(${window.scrollY * 0.12}px)`;
});

// Counter animation
const counters = document.querySelectorAll('[data-count]');
const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = +el.dataset.count;
        const suffix = el.dataset.suffix || '';
        let n = 0;
        const step = target / 50;
        const t = setInterval(() => {
            n = Math.min(n + step, target);
            el.textContent = Math.floor(n) + suffix;
            if (n >= target) clearInterval(t);
        }, 28);
        io.unobserve(el);
    });
}, { threshold: 0.5 });
counters.forEach(c => io.observe(c));

// AOS
if (typeof AOS !== 'undefined') {
    AOS.init({ duration: 700, once: true, offset: 60, easing: 'ease-out-cubic' });
}

// PDF Modal
function openPDF(url, title) {
    document.getElementById('pdfModalTitle').textContent = title;
    document.getElementById('pdfFrame').src = url;
    document.getElementById('pdfDownloadBtn').href = url;
    document.getElementById('pdfNewTabBtn').href = url;
    document.getElementById('pdfModal').classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closePDF() {
    document.getElementById('pdfModal').classList.remove('open');
    document.getElementById('pdfFrame').src = '';
    document.body.style.overflow = '';
}

document.getElementById('pdfModal')?.addEventListener('click', function(e) {
    if (e.target === this) closePDF();
});

// Team Profile Modals
const profileIds = { muni: 'profileMuni', ram: 'profileRam', subash: 'profileSubash', akash: 'profileAkash' };

function openProfile(id) {
    const modal = document.getElementById(profileIds[id]);
    if (!modal) return;
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closeProfile(id) {
    const modal = document.getElementById(profileIds[id]);
    if (!modal) return;
    modal.classList.remove('open');
    document.body.style.overflow = '';
}

document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    closePDF();
    Object.entries(profileIds).forEach(([key, modalId]) => {
        const el = document.getElementById(modalId);
        if (el?.classList.contains('open')) {
            el.classList.remove('open');
            document.body.style.overflow = '';
        }
    });
});

Object.entries(profileIds).forEach(([key, modalId]) => {
    document.getElementById(modalId)?.addEventListener('click', function(e) {
        if (e.target === this) closeProfile(key);
    });
});
