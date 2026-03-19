<script>
    import { onMount } from 'svelte';
    import Graph from "./Graph.svelte";

    let readings = null;
    let error = null;

    onMount(async () => {
        try {
            const res = await fetch("http://localhost:8000/readings");
            if (!res.ok) throw new Error("Backend returned an error");

            readings = await res.json();
        } catch (err) {
            error = "Could not load readings";
            console.error(err);
        }
    });
</script>

<h1>CGM Reader</h1>

<div class="topleft">
    <div class="box">
        <h2>Readings</h2>

        {#if error}
            <p style="color: red">{error}</p>

        {:else if !readings}
            <p>Loading…</p>

        {:else}
            <ul style="text-align: left;">
                {#each readings as r}
                    <li>
                        {new Date(r.timeTaken).toLocaleString()} - {r.glucoseLevel} mmol/L
                        
                    </li>
                {/each}
            </ul>
            {/if}
        </div>
    {#if readings}
        <Graph data={readings} />
    {/if}
</div>

<style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background: #f5f5f5;
    }
    .box {
        background: white;
        padding: 1rem 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        text-align: center;
        max-width: 40vw;
        max-height: 80vh;
        overflow-y: auto;
        margin-top: 10px;
    }
    .topleft {
        display: flex;
        justify-content: left;
        align-items: flex-start;
        background: #f5f5f5;
        gap: 2rem;
    }

</style>