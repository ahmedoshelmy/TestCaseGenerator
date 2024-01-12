# Introduction

This is implementation for the verifier that takes an input the N (number of packets) and vector of integers which
are the module numbers

# Instructions to run

- Open the Assignment_2 folder
- To Build, Run in the command

```
make
```

- Run the executable using

```
./PacketVerifier
``` 

- Check the output csv generated at ***packet_test_cases.csv***

# Code Explanation

- PacketVerifier Class is responsible for running the tester which takes the test case as an input and generates the CSV
- For each number in the array, if it's not range [1,N], then it's not valid
- Used % operator to check the circular relation between the module numbers

# Assumptions

- Each Module number depends on the previous module number only, not taking into consideration if the previous module
  was a valid number or not
- If a module is not valid, it continues does not stop 