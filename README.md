# Proof-of-History-Solana-Consensus-Algorithm-for-Blockchain-using-Python3
Proof of History is the primary consensus algorithm used in the popular blockchain architecture Solana. In this pet project, I have studied Solana in detail and created a true implemention of the Proof of History consensus algorithm used in Solana with Python 3.8 and compared it to the existing Proof of Work consensus algorithm.

In recent times, we are witnessing a global push in the tech industry towards the development of decentralized distributed systems for data transactions leading to significant advancements in the distributed ledger technology known as blockchain. However, the speed of transactions of most blockchain models is still significantly behind the speed of transactions provided by Visa or Master Card. Solana, a brainchild of Anatoly Yakovenko, has managed to change that with its unique consensus algorithm.

The heart of any blockchain model is the primary consensus algorithm used in its design. For any distributed computing system to work in sync, there need to be protocols in place so that the various coordinating processes can reach a common agreement on the data transmitted within the system to maintain system-wide authenticity. For blockchain, this work is done by consensus algorithms. Apart from maintaining the authenticity of the data in the blockchain, the consensus algorithms provide protection against a variety of attacks. In the original blockchain white paper by the pseudonymous person/persons Satoshi Nakamoto, the first blockchain consensus algorithm Proof-of-Work was documented. In this consensus algorithm, the SHA-256 hash output was subjected to a mathematical problem in which the numerical value of the hash generated has to be less than a pre-determined target. Such a suitable hash is rare and takes a lot of tries to find, thereby requiring computational work. This design was first used in Bitcoin and later on, adapted with modifications by various blockchain models.

There is another interpretation of Proof-of-Work. From elementary arithmetic, it is known that work and time are directly proportional. Therefore, in an isolated system, work is a measure of time. Hence, it can be derived that Proof-of-Work essentially functions as a decentralized clock for the system. This property of Proof-of-Work has been adopted into a new consensus algorithm called Proof-of-History, which is the core of the Solana blockchain. In the Proof-of-History, a cryptographic function is used to find the hash of a random number. The first hash output is used as the next input for which the hash is generated and the process continues iteratively. The state of the machine, the current output and the count are stored in fixed intervals. As we already discussed, the hash output record is irrefutable evidence of the passage of time, using the computational work done by the generating device as a decentralized clock.

This process is easier explained by a real-life analogy. Let’s suppose a Rubik’s cube is being solved. A photo of the cube is taken at the start and a picture is taken and printed. The picture is marked with the number “1”. The picture is kept beside the cube after a turn of the cube and another photo is taken such that both the cube and the first picture is in the frame. It is printed and marked with the number “2”. The process continues every turn. Now because a newer picture will always contain a previous picture inside, if any random number of pictures is picked, we can always arrange them in the correct sequence by the numbers and we will be able to identify the state of the cube over time using the sequence of pictures as a proof of passage of time. Here, the cube is analogous to the state of the machine, the picture analogous to the output hash and the number is basically the count.

We can see that with Proof-of-History, the provenance of the state is achieved without the need for any complicated mathematical problem, unlike Proof-of-Work. The process supports horizontal scaling allowing multiple generators to work in sync, resulting in very high scalability. While the hash sequence is generated with a single-core using the high clock-speed of a CPU, multiple cores of GPUs are parallelly used to verify multiple hashes at once. This allows Solana to have a block time of merely 400ms, which is several times faster than any other blockchain, resulting in unparalleled efficiency without any loss of security. Any attempt at tampering with the hash sequence will end up affecting all following hash outputs, creating an alternate history as directed by the “Butterfly effect” of Chaos Theory. This makes it essentially impossible for an attacker to predict a future hash. Apart from Proof-of-History, Solana also uses Proof-of-Replication as a scaling tool to store block verification history. Solana is written in Rust which is safer and has higher performance compared to C++ or Python.

The genius behind Solana’s design shows in its high scalability. Solana can maintain 50,000 transactions per second with 200 nodes which is far higher than Ethereum’s 20 transactions per second and Bitcoin’s 7 transactions per second. It even beats Visa’s estimated 1700 transactions per second. The resulting efficiency of Solana speaks for itself.
