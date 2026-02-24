export async function getStatus() {
    const res = await fetch("http://localhost:8000/status");
    return await res.json();
}