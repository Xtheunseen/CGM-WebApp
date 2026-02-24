<script>
    import { onMount } from 'svelte';

    let status;

    onMount(async () => {
        const res = await fetch("http://localhost:8000/status");
        status = await res.json();
    });
</script>

<p>Backend says: {status?.status}</p>
