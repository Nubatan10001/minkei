(function () {
    const root = document.documentElement;
    let ticking = false;

    function updateSceneryShift() {
        const scrollMax = Math.max(
            document.documentElement.scrollHeight - window.innerHeight,
            1
        );
        const progress = window.scrollY / scrollMax;
        const shift = -7 + progress * 14;

        root.style.setProperty("--scenery-shift", `${shift.toFixed(2)}vh`);
        ticking = false;
    }

    function requestUpdate() {
        if (!ticking) {
            window.requestAnimationFrame(updateSceneryShift);
            ticking = true;
        }
    }

    updateSceneryShift();
    window.addEventListener("scroll", requestUpdate, { passive: true });
    window.addEventListener("resize", requestUpdate);
})();
