// SPDX-License-Identifier: MIT
pragma solidity ^0.8.12;

contract EtherGameFixed {
    uint256 public targetAmount = 3 ether;
    uint256 public bal; // do not confuse with balance(), better to use a variable to compute balance instead of relaying on account.balance()
    address public winner;

    function deposit() public payable {
        require(msg.value == 1 ether, "You can only send 1 Ether");

        bal += msg.value;
        require(bal <= targetAmount, "Game is over");

        if (bal == targetAmount) {
            winner = msg.sender;
        }
    }

    function claimReward() public {
        require(msg.sender == winner, "Not winner");

        (bool sent, ) = msg.sender.call{value: bal}("");
        require(sent, "Failed to send Ether");
    }
}
