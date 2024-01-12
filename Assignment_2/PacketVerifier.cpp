
#include "PacketVerifier.h"


PacketVerifier::PacketVerifier() {

}

bool PacketVerifier::getTestCaseResult(int prevModule, int currentModule, int N) {
    if (currentModule > N || currentModule < 1) return false;
    prevModule--, currentModule--;
    return prevModule == currentModule || currentModule == (prevModule + 1) % N;
}

void PacketVerifier::run(int N, std::vector<int> &packets) {
    for (int i = 0; i < packets.size(); ++i) {
        if (packets[i] > N || packets[i] < 1) {
            std::cerr << "Invalid Input, all modules should be from 1 to N\n";
            return;
        }
    }
    std::vector<bool> result;
    if (packets.size()) {
        result.emplace_back(true);
    }
    for (size_t i = 1; i < packets.size(); ++i) {
        int currentModule = packets[i];
        int prevModule = packets[i - 1];

        result.emplace_back(getTestCaseResult(prevModule, currentModule, N));
    }

    generateCSV(N, packets, result);
}

void PacketVerifier::generateCSV(int N, std::vector<int> packets, std::vector<bool> result) {
    const std::string csvFilePath = "packet_test_cases.csv";

    std::ofstream outputFile(csvFilePath);

    if (!outputFile.is_open()) {
        std::cerr << "Error opening file: " << csvFilePath << std::endl;
        return;
    }

    std::vector<std::vector<std::string>> data;
    std::vector<std::string> columns = {"PacketID", "ModuleNumber", "ValidModule"};

    data.emplace_back(columns);


    for (int i = 0; i < packets.size(); ++i) {
        std::vector<std::string> row;
        row.emplace_back(std::to_string(i + 1));
        row.emplace_back(std::to_string(packets[i]));
        row.emplace_back(result[i] ? "Yes" : "No");

        data.emplace_back(row);
    }

    for (const auto &row: data) {
        for (size_t i = 0; i < row.size(); ++i) {
            outputFile << row[i];
            if (i < row.size() - 1) {
                outputFile << ",";
            }
        }
        outputFile << std::endl;
    }

    outputFile.close();

    std::cout << "Data has been written to " << csvFilePath << std::endl;
}