## 1. Introduction

The provided code is responsible for generating test cases. The below Design is proposed general design for testing the
server feature

## 2. Instructions to run:

Open the folder **Assignment_1**, then run the following command

```shell
python main.py
```

# Design for Testing Process

This plan outlines a comprehensive approach to testing the server's configuration feature.

## 1. Test Objectives:

Testing that the following features are working properly.
This features can be tested on a small level for the server only or a general level when the system is runnnig.

- ### Features to be tested
    - Allowing 2 clients to be connected at the same time to the same server
    - The first connected client becomes a master client instantaneously
    - The master client can edit the configurations
    - The second connected client does not have access to change the options
    - The server does not show an error if the second client tries to configure the server with same options
    - The default options are applied if the master client did not configure options
    - Two clients trying to connect simultaneously (Race conditions)

## 2. Testing Requirements:

- Access to create and run server instances
- Access to create and run client instances
- Access to connect the clients to the run
- Access to the errors output of the server
- Access to read the state of the options in the server

## 3. Testing Strategy:

Employ a combination of black-box testing (e.g. e2e testing) and white-box testing (e.g. unit tests) for comprehensive
coverage.

## 4. Testing Techniques:

- ### Unit Testing
    - Methods:
        - Employ unit tests for individual functions within the server codebase.
        - Given the codebase of the server and using the testcase generator, the created test cases will be used to test
          the functions within the server by passing options to the functions and expecting the success or error output.
        -
    - Purpose:
        - Verify the correctness of each function in isolation, ensuring they perform as expected
- ### End-to-End Testing
    - This can be achieved by creating or mocking clients that gets connected to the server
    - It requires a running instance of the server to be tested with ability to change
    - Diagram below is showing the flow of these tests:

![Blank diagram.png](ServerTestE2E.png)

- ### Stress Testing
    - This can be achieved by creating multiple clients and trying to connect them to the server at the same time

## 5. Testing Deliverables:

- Test cases
- Test scripts
- Unit Test Reports (How many passed and failed ? )
- Performance Test Reports
- Test Coverage

## 6. Testing Tools:

Tools can be used to automate the test cases and generate reports like:

- pytest
- selenium

## 7. Detailed Test Suite and scenarios:

## Proposed Test Suite 

### Master Client Configuration

- **TC1.1:** Connect master client, set both `buffer_data` and `enable_timeout` to `true`.
    - Verify server accepts and applies configurations.
- **TC1.2:** Connect master client, set `buffer_data` to `false`, leave `enable_timeout` unset.
    - Verify server applies `buffer_data=false`, `enable_timeout=true`.
- **TC1.3:** Connect master client, don't set any parameters.
    - Verify server uses default values (`buffer_data=true`, `enable_timeout=true`).

### Slave Client Configuration

- **TC2.1:** Connect slave client, attempt to change `buffer_data` to `false` (different from master's setting).
    - Verify server rejects change and returns error message.
- **TC2.2:** Connect slave client, attempt to set same values as master client.
    - Verify server accepts settings without errors.

### Master Client Reconnection

- **TC3.1:** Disconnect master client, connect new master client, set different configuration values.
    - Verify server accepts new configuration from new master client.

### Error Handling

- **TC4.1:** Attempt to set invalid configuration values (non-Boolean).
    - Verify server handles invalid values gracefully (e.g., returns errors).
- **TC4.2:** Disconnect master client unexpectedly.
    - Verify server maintains last configured values and allows new master client to reconfigure.

### Simultaneous Client Connections

- **TC5.1:** Activate two clients to connect simultaneously.
    - Verify server correctly assigns master status to one client and slave status to the other.
    - Analyze server logs to confirm accurate handling of race conditions.
    - Validate handling of race conditions

### Performance

- **TC6.1:** Measure configuration setup time under different load conditions.
- **TC6.2:** Measure configuration change speed under different load conditions.

### Security (if applicable)

- **TC7.1:** Attempt unauthorized configuration changes.
    - Verify server rejects unauthorized attempts and logs security events.

### Integration Testing

- **TC9.1:** Test interaction between server's configuration module and other components.
    - Verify configurations are applied correctly across components.
    - Ensure data flow and communication adhere to configured settings.

### End-to-End Testing

- **TC10.1:** Connect master client, set configurations, perform client actions that rely on settings.
    - Verify server behavior aligns with configured values from the client's perspective.
- **TC10.2:** Connect slave client, attempt actions that might be affected by configurations.
    - Confirm server enforces configuration restrictions for slave client.
- **TC10.3:** Simulate real-world usage scenarios with both client types interacting with the server.
    - Verify overall system behavior matches expectations under various conditions.

### Error Handling in Client Interactions

- **TC11.1:** Attempt invalid configurations from the client.
    - Verify server returns appropriate error messages to the client.
- **TC11.2:** Disconnect clients unexpectedly during configuration or normal operations.
    - Test server's resilience and handling of unexpected client behavior.

### Performance in Client Interactions

- **TC12.1:** Measure client-perceived response times for configuration changes and data operations under different load
  conditions.
- **TC12.2:** Evaluate overall system performance from the client's perspective, including configuration setup and
  normal operations.
