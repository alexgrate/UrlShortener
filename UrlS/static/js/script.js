const copy_url = ()=>{
    const short_url = document.getElementById("short-url").innerText
    navigator.clipboard.writeText(short_url);
}