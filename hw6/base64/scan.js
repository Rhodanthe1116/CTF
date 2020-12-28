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
    // Note: we use the crlfDelay option to recognize all instances of CR LF
    // ('\r\n') in input.txt as a single line break.
    for await (const file of rl) {
        // Each line in input.txt will be successively available here as `line`.

        let formData = new URLSearchParams()
        formData.append('url', `file://${file}`);

        fetch(`http://base64image.splitline.tw:8894/?page=result`, {
            method: 'POST',
            body: formData
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

                    const imgsrc = dom.window.document.querySelector(selector).getAttribute('src')
                    // const problemList = Array.from(problemNodeList).map((p) => p.textContent);
                    const base64 = imgsrc.split(',')[1]


                    let bufferObj = Buffer.from(base64, "base64");
                    decoded = bufferObj.toString("utf8");
                }

                if (decoded.length === 0) {
                    throw new Error('empty')
                }

                const dir = file.split('/').splice(0,)

                fs.promises.mkdir(`./output/${path.dirname(file)}`, { recursive: true })
                    .then(x => {
                        const filename = file.split('/').reverse()[0]
                        fs.writeFile(`./output/${file}`, decoded, function (err) {
                            if (err) return console.log(err);
                            console.log(`${file}`);
                        });
                    })
                    .catch(err => {
                        console.log(err);

                    })

            }).catch(err => {
                console.log(`ERR! ${file}`);
                // console.log(err);

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