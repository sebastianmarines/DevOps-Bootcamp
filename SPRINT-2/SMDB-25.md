# Networking

Data flow in networks is organized in layers, each layer is implemented individually, and each layer only deals with the task that it is supposed to execute.

## OSI Model

The Open System Interconnection model was made to create a standardized network protocol, so that all networks were compatible between them.

This model standardizes the way each layer communicate with other layers, fosters modularity, and ensures interoperability.

### Layers

7. **Application Layer**: This layer supports user and application tasks and overall system management, including resource sharing, file transfers, remote file servers and database and network management.
6. **Presentation Layer**: This layer translates and converts transmitted encoded data into formats that can be understood and manipulated by users.
5. **Session Layer**: Establishes and controls system-dependent aspects of communication sessions provided by the *Transport layer* and the logical functions running under the operating system in a participant node.
4. **Transport Layer**: Provides end-to-end control of a communication session once the path has been established, which enables the reliable and sequential exchange of data independent of both the systems that are communicating and their locations in the network.
3. **Network-Control Layer**: Addresses messages, sets up the path between communicating nodes, routes messages across intervening nodes to their destinations and controls the flow of messages between nodes.
2. **Data-Link Layer**: Establishes an error free communication path between network nodes over the physical channel, frames messages for transmission, checks the integrity of received messages, manages access to and use of the channel and ensures the sequence of transmitted data.
1. **Physical Layer**: Defines the electrical and mechanical aspects of interfacing to a physical medium for transmitting data, as well as setup, maintenance and disconnection of physical links. This layer includes the software driver for each communications device, plus the hardware itself--interface devices, modems and communication lines.

### Protocol Data Units

- **Application Layer**: Data
- **Presentation Layer**: Data
- **Session Layer**: Data
- **Transport Layer**: Segments
- **Network-Control Layer**: Packets
- **Data-Link Layer**: Frames
- **Physical Layer**: Bits


## TCP/IP

### Comparison between OSI model and TCP/IP

| OSI          | TCP/IP         |
| ------------ | -------------- |
| Application  | Application    |
| Presentation | Application    |
| Session      | Application    |
| Transport    | Transport      |
| Network      | Internet       |
| Data-Link    | Network Access |
| Physical     | Network Access |

The TCP/IP protocol was created by the US Department of Defense because they wanted a network that could be reliable in any circumstance, even in a nuclear war and was designed as an open standard.

### The model

- **Application**: Represents user data as well as controlling data encoding and data sending. Examples of protocols in this layer includes *FTP, HTTP, SMTP, DNS*
- **Transport**: Allows communication between devices in different networks. Examples of protocol in this layers includes *TCP* and *UDP*
- **Internet**: Establishes the best route through the network.
- **Network Access**: Controls hardware devices.


