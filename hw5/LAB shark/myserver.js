if (command &&
    command.indexOf("shark") == -1 &&
    command.length < 3 &&
    command == "Baby shark, doo doo doo doo doo doo") {

}

if (command) {
    console.log("command")
}

if (command.indexOf("shark") == -1) {
    console.log("-1")
}

if (command.length < 3) {
    console.log("command.length < 3")
}

if (command == "Baby shark, doo doo doo doo doo doo") {
    console.log("command == Baby shark, doo doo doo doo doo doo")
}
