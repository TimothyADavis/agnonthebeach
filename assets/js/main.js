---
---

{% include js/conference.js %}
(() => {
    const map = window.conference.map;

    if (typeof map !== 'undefined') {
        let main_station = L.marker([47.37785, 8.54035], {
            icon: L.divIcon({
                className: '',
                html: '<span class="fas fa-train"></span> Main Station',
                iconSize: [120, 56]
            })
        }).addTo(map);
    }
})();