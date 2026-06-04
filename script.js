// Website status (demo)
document.getElementById("status").innerText = "All Websites Running ✔️";

// Graph using Chart.js
const ctx = document.getElementById('chart').getContext('2d');

new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [{
            label: 'Response Time (ms)',
            data: [120, 150, 180, 90, 110, 200, 160],
            borderColor: 'blue',
            fill: false
        }]
    }
});