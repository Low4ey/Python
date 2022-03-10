function login(token) {
    setInterval(() => {
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
    location.reload();
    }, 2500);
    }
    
    login('ODY2ODkwNDMzOTYyNTczODQ1.YcCD1w.Zw12mS0FzP5rF8ZwRyO8Rl3WdGE')