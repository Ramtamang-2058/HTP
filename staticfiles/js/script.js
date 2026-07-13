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

// ─── Video tab switcher ───────────────────
const videoSources = [
    '/video/building_base_robot.mov',
    '/video/handshke_robot.mov'
];

function switchVideo(index) {
    const video = document.getElementById('mainVideo');
    if (!video) return;

    // Update tabs
    document.querySelectorAll('.video-tab').forEach((tab, i) => {
        tab.classList.toggle('active', i === index);
    });

    // Fade out, swap source, fade in
    video.style.opacity = '0';
    video.style.transition = 'opacity 0.3s ease';

    setTimeout(() => {
        video.pause();
        const source = video.querySelector('source');
        if (source) source.src = videoSources[index];
        video.load();
        video.style.opacity = '1';
    }, 300);
}

// ─── INSTAGRAM STORIES SYSTEM ─────────────
let currentStoryIndex = 0;
let storyTimer = null;
let storyProgressInterval = null;
let storyDuration = 5000; // 5s default
let storyStartTime = 0;
let storyPaused = false;
let elapsed = 0;

function openStory(index) {
    if (typeof storiesData === 'undefined' || !Array.isArray(storiesData) || !storiesData.length) return;
    
    // Parse index strictly
    index = parseInt(index, 10);
    if (isNaN(index)) return;

    currentStoryIndex = index;
    const modal = document.getElementById('storyModal');
    if (!modal) return;
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    loadStorySlide(index);
}

function closeStory() {
    const modal = document.getElementById('storyModal');
    if (!modal) return;
    modal.classList.remove('open');
    document.body.style.overflow = '';
    
    // Pause video if playing
    const video = document.getElementById('storyModalVideo');
    if (video) video.pause();
    
    clearStoryTimers();
}

function clearStoryTimers() {
    if (storyTimer) clearTimeout(storyTimer);
    if (storyProgressInterval) clearInterval(storyProgressInterval);
    const progressFill = document.getElementById('storyProgress');
    if (progressFill) progressFill.style.width = '0%';
    elapsed = 0;
    storyPaused = false;
}

function loadStorySlide(index) {
    clearStoryTimers();
    
    index = parseInt(index, 10);
    if (isNaN(index) || index < 0 || index >= storiesData.length) {
        closeStory();
        return;
    }
    
    currentStoryIndex = index;
    const item = storiesData[index];
    if (!item) {
        closeStory();
        return;
    }
    
    const avatar = document.getElementById('storyModalAvatar');
    const title = document.getElementById('storyModalTitle');
    const caption = document.getElementById('storyModalCaption');
    const img = document.getElementById('storyModalImage');
    const videoWrap = document.getElementById('storyVideoWrapper');
    const video = document.getElementById('storyModalVideo');
    
    if (avatar) avatar.src = item.thumbnailUrl || '';
    if (title) title.textContent = item.title || '';
    if (caption) caption.textContent = item.caption || '';
    
    if (item.mediaType === 'video') {
        img.style.display = 'none';
        videoWrap.style.display = 'flex';
        video.src = item.mediaUrl;
        video.load();
        
        video.onloadedmetadata = function() {
            storyDuration = video.duration * 1000 || 6000;
            startStoryProgressBar();
        };
        video.play().catch(() => {
            storyDuration = 6000;
            startStoryProgressBar();
        });
        
        video.onended = function() {
            nextStory();
        };
    } else {
        videoWrap.style.display = 'none';
        video.pause();
        img.style.display = 'block';
        img.src = item.mediaUrl;
        storyDuration = 5000; // 5s for images
        startStoryProgressBar();
        
        storyTimer = setTimeout(() => {
            nextStory();
        }, storyDuration);
    }
}

function startStoryProgressBar() {
    const progressFill = document.getElementById('storyProgress');
    if (!progressFill) return;
    
    const start = Date.now();
    storyStartTime = start;
    
    storyProgressInterval = setInterval(() => {
        if (storyPaused) return;
        const currentElapsed = Date.now() - start - elapsed;
        const percentage = Math.min((currentElapsed / storyDuration) * 100, 100);
        progressFill.style.width = percentage + '%';
        if (percentage >= 100) {
            clearInterval(storyProgressInterval);
        }
    }, 30);
}

function prevStory() {
    if (currentStoryIndex > 0) {
        loadStorySlide(currentStoryIndex - 1);
    } else {
        closeStory();
    }
}

// Global scope definition so button clicks work
window.prevStory = prevStory;
window.nextStory = nextStory;
window.openStory = openStory;
window.closeStory = closeStory;

function nextStory() {
    if (currentStoryIndex < storiesData.length - 1) {
        loadStorySlide(currentStoryIndex + 1);
    } else {
        closeStory();
    }
}

// Pause/Play story on tap/hold
const storyMediaContainer = document.querySelector('.story-media-container');
if (storyMediaContainer) {
    storyMediaContainer.addEventListener('mousedown', () => {
        storyPaused = true;
        const video = document.getElementById('storyModalVideo');
        if (video && !video.paused) video.pause();
    });
    storyMediaContainer.addEventListener('mouseup', () => {
        storyPaused = false;
        const video = document.getElementById('storyModalVideo');
        if (video && video.paused) video.play().catch(()=>{});
    });
    storyMediaContainer.addEventListener('touchstart', () => {
        storyPaused = true;
        const video = document.getElementById('storyModalVideo');
        if (video && !video.paused) video.pause();
    });
    storyMediaContainer.addEventListener('touchend', () => {
        storyPaused = false;
        const video = document.getElementById('storyModalVideo');
        if (video && video.paused) video.play().catch(()=>{});
    });
}


// ─── AUTO-SLIDING LAB PHOTO GALLERY ──────
let currentSlideIndex = 0;
let slideInterval = null;

function setSlide(index) {
    currentSlideIndex = index;
    const track = document.getElementById('slideshowTrack');
    if (!track) return;
    
    // Move track
    track.style.transform = `translateX(-${index * 25}%)`;
    
    // Update dots
    document.querySelectorAll('.slide-dot').forEach((dot, i) => {
        dot.classList.toggle('active', i === index);
    });
}

function startSlideshow() {
    if (slideInterval) clearInterval(slideInterval);
    slideInterval = setInterval(() => {
        currentSlideIndex = (currentSlideIndex + 1) % 4;
        setSlide(currentSlideIndex);
    }, 4000);
}

// Expose setSlide globally
window.setSlide = setSlide;

// Initialize slideshow
document.addEventListener('DOMContentLoaded', () => {
    startSlideshow();
});
