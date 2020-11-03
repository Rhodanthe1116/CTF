const fs = require('fs');
const lib = require('./lib')(require('./config'));

async function main() {
    const abi = JSON.parse(fs.readFileSync('./Bet.json'));
    const address = '0xFc999651900C8AA9A70Ab50d951Da85a0b920465'
    let bet = lib.contract(address, abi);
    console.log('player: ', await bet.storage(0));
    console.log('seed: ', await bet.storage(1));
    console.log('-----------------');


    const hackAbi = JSON.parse(fs.readFileSync('./HackBet.json'));
    const hackAddress = '0x9a3285654c171a74f87683939db5ba3be69deee5'
    let hack = lib.contract(hackAddress, hackAbi);
    // console.log(await hack.storage(0));
    console.log('target: ', await hack.storage(0));
    console.log('seed: ', await hack.storage(1));
    console.log('received: ', await hack.storage(2));


};

main();