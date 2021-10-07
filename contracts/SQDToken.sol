// contracts/SQDToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract SQDToken is ERC20 {
    uint256 private constant TOTAL_SUPPLY = 10**27;
    string private constant NAME = "Squid Token";
    string private constant SYMBOL = "SQD";

    constructor(uint256 initialSupply) ERC20(NAME, SYMBOL) {
        _mint(msg.sender, initialSupply);
    }
}
