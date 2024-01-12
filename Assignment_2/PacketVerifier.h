#include <iostream>
#include <fstream>
#include <vector>
#include <string>

class PacketVerifier {

private:
    void generateCSV(int N ,std::vector<int> packets, std::vector<bool> result);

    bool getTestCaseResult(int prevModule, int currentModule, int N);

public:
    PacketVerifier();

    void run(int N, std::vector<int> &packets);


};


