const fs = require('fs');
const lib = require('./lib')(require('./config'));

async function main() {
    let c = lib.contract('0x21546F53AC81DDfc2b618D5617d173e43661366c', JSON.parse(fs.readFileSync('Private.abi')));
    console.log(await challenge.storage(0));
};

main();