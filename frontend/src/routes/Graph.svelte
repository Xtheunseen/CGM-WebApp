<script>
    export let data = [];

    const points = data.map(d => ({
        x: new Date(d.timeTaken).getTime(),
        y: d.glucoseLevel
    }));

    const minX = Math.min(...points.map(p => p.x));
    const maxX = Math.max(...points.map(p => p.x));
    const minY = Math.min(...points.map(p => p.y));
    const maxY = Math.max(...points.map(p => p.y));

    const width = 600;
    const height = 400;
    const padding = 40;

    const scaleX = x =>
        padding + ((x - minX) / (maxX-minX) * width - padding * 2);
    
    const scaleY = y =>
        height - padding - ((y - minY) / (maxY - minY)) * (height - padding * 2);

    const linePath = points
    .map((p, i) => `${i === 0 ? "M" : "L"} ${scaleX(p.x)} ${scaleY(p.y)}`)
    .join(" ");
</script>

<svg {width} {height} style="border: 1px solid #ccc; margin-top: 20px;">
  <!-- Line -->
  <path d={linePath} fill="none" stroke="#4a90e2" stroke-width="2" />

  <!-- Dots -->
  {#each points as p}
    <circle cx={scaleX(p.x)} cy={scaleY(p.y)} r="4" fill="#e24a4a" />
  {/each}
</svg>
