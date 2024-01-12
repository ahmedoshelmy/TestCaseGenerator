#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#include "PacketVerifier.h"


int main() {

    std::cout << "Started generating test cases\n";

    PacketVerifier packetVerifier;

    int N = 4;
    std::vector<int> packets = {1, 3, 4, 4};

    packetVerifier.run(N, packets);

    return 0;
}
