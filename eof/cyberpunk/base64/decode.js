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

decodeConsole()