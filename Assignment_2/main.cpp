#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#include "PacketVerifier.h"


int main() {

    std::cout << "Started generating test cases\n";

    PacketVerifier packetVerifier;

    int N = 4;
    std::vector<int> packets = {4,4,4,5, 1, 2, 3};

    packetVerifier.run(N, packets);

    return 0;
}
