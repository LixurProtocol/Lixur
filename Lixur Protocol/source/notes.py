"""
Estimated Testnet Beta Release: March 2022 (But progress greatly depends on how fast we can implement a functional peer to peer network, if we can do this in two days,
then 7-14 days after should be the release date hopefully). PS: Update the code on GitHub before you post this to the Discord Server.
----------------------------------------------------------------------------------------------------------------------------------------------------------
Tasks:
*: Associate readable addresses.
*: Solve cryptocurrency forge problem
*: Nano everyone has their ledger thing
*: Address pair
*: Indicate you have windows on the readme
*: Focus on recruiting developers, this time search up open-sourced developers or open-source blockchain developers.

*: We need to establish a peer to peer connection framework where multiple devices can interact and append to the ledger and network. We will know we have
completed this when I can run the program from multiple devices and they can submit their own transactions and on the /node page, there should be
two or more nodes available and can send any node on the network a message back and forth. After this, find a way to retrieve the SHA512 ID from the code
but if not, then give them your own ID. The IP Addresses MUST be IPv6! (A week maybe, I don't know much about networking).
*: Make the Enchanted Consensus Weighted and then add that logic to the is_valid_transaction() function in graph.py. (A few days hopefully)
*: Once networking is achieved, we need to develop the framework in make_transaction() to have the ability to transfer funds. (Three days maybe)
*: Once that is achieved, have the readable addresses be related to the public address of the wallet. (One to two days at most)
*: Add your JIT Compiler throughout the code, whether this would be RustPython or Numba (About a dozen hours at most, research as biggest time waster)
*: Once that is done, clean up everywhere and simplify the code, look for anything else that needs to
be simplified, modified or otherwise added/removed. Then probably make a nice HTML page for it and you can release the Lixur Testnet Beta Version 1.0.0 (Worst case, a week)

People can spam the network sending transactions to themselves.

theres a small chance only tw transactions will appear, probably due to an error appending the transaction to the ledger.

[!] This will be a Testnet Beta Version, the LXR will be worth nothing (Will have legit value in the Main-net) and expect chaos, haywire, bugs, malfunctions etc.
(Until Main-net Version/Main-net Beta Version is released, likely somewhere around Late 2022 to Early 2023. The purpose of the Testnet Beta is to test functionality.

"""
