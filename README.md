Dont relay on address(this).balance, use a declared variable (bal) to compute the balance of ether sent.

On the EtherGame, Attack contracts, the EtherGame is blocked by sending 7 ethers using selfdestruct in Attack.attack

On the EtherGameFixed, AttackFixed contracts, the EtherGameFixed is not blocked by sending 1 ethers using selfdestruct in AttackFixed.attack
Instead, the balance() reports 4 ethers, but bal reports 3 ethers and the winner is set and can claim the reward
