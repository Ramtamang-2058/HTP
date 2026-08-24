/* High Tech Pioneer — minimal progressive enhancement. */
(function () {
    'use strict';

    /* Footer year */
    var year = document.getElementById('year');
    if (year) year.textContent = String(new Date().getFullYear());

    /* Mobile navigation */
    var toggle = document.querySelector('.nav-toggle');
    var mobileNav = document.getElementById('mobile-nav');
    if (toggle && mobileNav) {
        toggle.addEventListener('click', function () {
            var open = mobileNav.classList.toggle('open');
            if (open) mobileNav.removeAttribute('hidden');
            else mobileNav.setAttribute('hidden', '');
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && mobileNav.classList.contains('open')) {
                mobileNav.classList.remove('open');
                mobileNav.setAttribute('hidden', '');
                toggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    /* Stories scroller arrows (desktop) */
    document.querySelectorAll('.stories-arrow').forEach(function (button) {
        var strip = document.querySelector('[data-stories]');
        if (!strip) return;
        button.addEventListener('click', function () {
            var card = strip.querySelector('.story');
            var step = card ? card.getBoundingClientRect().width + 20 : 320;
            strip.scrollBy({ left: step * Number(button.dataset.scroll), behavior: 'smooth' });
        });
    });

    /* Lazy video loading: only fetch the .mov when a visitor chooses to play. */
    document.querySelectorAll('.story-media[data-video]').forEach(function (link) {
        link.addEventListener('click', function (event) {
            var video = link.querySelector('video[data-src]');
            if (!video) return;
            event.preventDefault();
            if (!video.getAttribute('src')) {
                video.setAttribute('src', video.getAttribute('data-src'));
            }
            var playing = video.play();
            if (playing && typeof playing.catch === 'function') {
                playing.catch(function () { /* autoplay refused; native controls remain */ });
            }
            video.setAttribute('controls', 'controls');
            var playBadge = link.querySelector('.story-play');
            if (playBadge) playBadge.remove();
            link.removeAttribute('href');
        });
    });
})();
