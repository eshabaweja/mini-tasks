<b>What is the main purpose of an operating system? Discuss different types? </b>- An operating system (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs. So it manages the computer’s memory, processes, devices, files, and security aspects of the system. It also allows us to communicate with the computer without knowing how to speak the computer’s language. Without an operating system, a computer is not useful. Types of operating system:

- Batch OS
- Distributed OS
- Multitasking OS
- Network OS
- Real-Time OS
- Mobile OS

Reference: https://www.geeksforgeeks.org/types-of-operating-systems/

<b>What is a socket, kernel and monolithic kernel ? </b>- Socket:A socket is defined as an endpoint for communication, A pair of processes communicating over a network employ a pair of sockets ,one for each process. A socket is identified by an IP address concatenated with a port number. The server waits for incoming client requests by listening to a specified port. Once a request is received, the server accepts a connection from the client socket to complete the connection.

- Kernel is the central core component of an operating system that manages operations of computer and hardware. Kernel Establishes communication between user level application and hardware. Manages memory and CPU time. Decides state of incoming processes. Controls Disk, Memory, Task Management
- Monolithic Kernel (provides good performance but lots of lines of code)It is one of the types of kernel where all operating system services operate in kernel space. It has dependencies between system components. It has huge lines of code which is complex.Example : Unix, Linux, Open VMS, XTS-400 etc.


<b>Difference between process and program and thread? Different types of process. </b>- Process:Process is an instance of an executing program. For example, we write our computer programs in a text file and when we execute this program, it becomes a process which performs all the tasks mentioned in the program.
- Program:Program is a set of instructions to perform a certain task. Eg: chrome.exe, notepad.exe
- Thread:Thread is a path of execution within a process. A thread is also known as a lightweight process. The idea is to achieve parallelism by dividing a process into multiple threads. For example,Word processor uses multiple threads: one thread to format the text, another thread to process inputs.

<b>Define virtual memory, thrashing, threads.  </b>- Virtual Memory:A computer can address more memory than the amount physically installed on the system. This extra memory is actually called virtual memory and it is a section of a hard disk that’s set up to emulate the computer’s RAM.The main visible advantage of this scheme is that programs can be larger than physical memory. Virtual memory serves two purposes. First, it allows us to extend the use of physical memory by using a disk. Second, it allows us to have memory protection, because each virtual address is translated to a physical address.

- Thrashing: Thrashing is a condition or a situation when the system is spending a major portion of its time in servicing the page faults, but the actual processing done is very negligible. High degree of multiprogramming(if number of processes keeps on increasing in the memory), lack of frames (if a process is allocated too few frames, then there will be too many and too frequent page faults) causes Thrashing.
- Threads:A thread is a single sequential flow of execution of tasks of a process so it is also known as thread of execution or thread of control.


<b>What is RAID ? Different types. </b>- RAID, or “Redundant Arrays of Independent Disks” is a technique which makes use of a combination of multiple disks instead of using a single disk for increased performance, data redundancy or both.Data redundancy, although taking up extra space, adds to disk reliability. This means, in case of disk failure, if the same data is also backed up onto another disk, we can retrieve the data and go on with the operation.


<b>What is a deadlock? Different conditions to achieve a deadlock. </b>- A Deadlock is a situation where each of the computer processes waits for a resource which is being assigned to some other process. In this situation, none of the processes gets executed since the resource it needs is held by some other process which is also waiting for some other resource to be released.

**How deadlock is achieved**:  Deadlock happens when Mutual exclusion, hold and wait, No preemption and circular wait occurs simultaneously.

**Necessary Conditions for deadlock:**

- Mutual Exclusion
- Hold and Wait
- No preemption
- Circular Wait


<b>What is fragmentation? Types of fragmentation. </b>- Fragmentation:An unwanted problem in the operating system in which the processes are loaded and unloaded from memory, and free memory space is fragmented. Processes can’t be assigned to memory blocks due to their small size, and the memory blocks stay unused. It is also necessary to understand that as programs are loaded and deleted from memory, they generate free space or a hole in the memory. These small blocks cannot be allotted to new arriving processes, resulting in inefficient memory use.
- The conditions of fragmentation depend on the memory allocation system. As the process is loaded and unloaded from memory, these areas are fragmented into small pieces of memory that cannot be allocated to incoming processes. It is called fragmentation.
- Types of fragmentation: 1. Internal 2. External


<b>What is spooling ? </b>- SPOOL is an acronym for simultaneous peripheral operations online. Spooling is a process in which data is temporarily held to be used and executed by a device, program, or system.In spooling, there is no interaction between the I/O devices and the CPU. That means there is no need for the CPU to wait for the I/O operations to take place. Such operations take a long time to finish executing, so the CPU will not wait for them to finish.The biggest example of Spooling is printing. The documents which are to be printed are stored in the SPOOL and then added to the queue for printing. During this time, many processes can perform their operations and use the CPU without waiting while the printer executes the printing process on the documents one-by-one.


<b>What is semaphore and mutex (Differences might be asked)? Define Binary semaphore. </b>

<b>Belady’s Anomaly</b>- Bélády’s anomaly is the name given to the phenomenon where increasing the number of page frames results in an increase in the number of page faults for a given memory access pattern.
- Solution to fix Belady’s Anomaly:Implementing alternative page replacement algo helps eliminate Belady’s Anomaly.. Use of stack based algorithms, such as Optimal Page Replacement Algorithm and Least Recently Used (LRU) algorithm, can eliminate the issue of increased page faults as these algorithms assign priority to pages


<b>Starving and Aging in OS</b>- Starving/Starvation(also called Lived lock): Starvation is the problem that occurs when low priority processes get jammed for an unspecified time as the high priority processes keep executing. So starvation happens if a method is indefinitely delayed.
- Solution to Starvation : Ageing is a technique of gradually increasing the priority of processes that wait in the system for a long time.


<b>Why does trashing occur? </b>- High degree of multiprogramming(if number of processes keeps on increasing in the memory) , lack of frames(if a process is allocated too few frames, then there will be too many and too frequent page faults.) causes Thrashing.


<b>What is paging and why do we need it? </b>- Paging is a memory management scheme that eliminates the need for contiguous allocation of physical memory. This scheme permits the physical address space of a process to be non – contiguous.Paging is used for faster access to data. When a program needs a page, it is available in the main memory(RAM) as the OS copies a certain number of pages from your storage device to main memory. Paging allows the physical address space of a process to be noncontiguous.


<b>Demand Paging, Segmentation </b>- Demand paging is a method of virtual memory management which is based on the principle that pages should only be brought into memory if the executing process demands them. This is often referred to as lazy evaluation as only those pages demanded by the process are swapped from secondary storage to main memory.So demand paging works opposite to the principle of loading all pages immediately.
- Segmentation is a memory management technique in which the memory is divided into the variable size parts. Each part is known as a segment which can be allocated to a process.
- The details about each segment are stored in a table called a segment table. Segment table is stored in one (or many) of the segments.
- Segment table contains mainly two information about segment:
- Base: It is the base address of the segmentLimit: It is the length of the segment.


<b>Real Time Operating System, types of RTOS. </b>- A real-time operating system (RTOS) is a special-purpose operating system used in computers that has strict time constraints for any job to be performed and is intended to serve real time applications that possess data as it comes in , typically without buffer delays.
- Types of RTOS:
- Hard RTOS
- Firm RTOS
- Soft RTOS


<b>Difference between main memory and secondary memory. </b>

<b>Dynamic Binding </b>- Static binding happens when the code is compiled, while dynamic bind happens when the code is executed at run time.
- Static Binding:When a compiler acknowledges all the information required to call a function or all the values of the variables during compile time, it is called “static binding”. As all the required information is known before runtime, it increases the program efficiency and it also enhances the speed of execution of a program. Static Binding makes a program very efficient, but it declines the program flexibility, as ‘values of variable’ and ‘function calling’ are predefined in the program. Static binding is implemented in a program at the time of coding. Overloading a function or an operator is the example of compile time polymorphism i.e. static binding.
- Dynamic Binding Calling a function or assigning a value to a variable, at run-time is called “Dynamic Binding”. Dynamic binding can be associated with run time ‘polymorphism’ and ‘inheritance’ in OOP. Dynamic binding makes the execution of a program flexible as it can decide what value should be assigned to the variable and which function should be called, at the time of program execution. But as this information is provided at run time it makes the execution slower as compared to static binding.


<b>FCFS Scheduling </b>

<b>SJF Scheduling </b>

<b>SRTF Scheduling </b>- SRTF Scheduling is a preemptive version of SJF scheduling. In SRTF, the execution of the process can be stopped after a certain amount of time. At the arrival of every process, the short term scheduler schedules the process with the least remaining burst time among the list of available processes and the running process.


<b>LRTF Scheduling </b>- This is a preemptive version of Longest Job First (LJF) scheduling algorithm. In this scheduling algorithm, we find the process with the maximum remaining time and then process it. We check for the maximum remaining time after some interval of time(say 1 unit each) to check if another process having more Burst Time arrived up to that time.


<b>Priority Scheduling </b>- Priority Scheduling is a method of scheduling processes that is based on priority. In this algorithm, the scheduler selects the tasks to work as per the priority.
- The processes with higher priority should be carried out first, whereas jobs with equal priorities are carried out on a round-robin or FCFS basis. Priority depends upon memory requirements, time requirements, etc.


<b>Round Robin Scheduling </b>- In Round-robin scheduling, each ready task runs turn by turn only in a cyclic queue for a limited time slice. This algorithm also offers starvation free execution of processes. Widely used preemptive scheduling method in traditional OS. All the jobs get a fair allocation of CPU. Cons include : Finding a correct time quantum is a quite difficult task in this system, Round-robin scheduling doesn’t give special priority to more important tasks.


<b>Producer Consumer Problem </b>- About Producer-Consumer problem: The Producer-Consumer problem is a classic problem that is used for multi-process synchronisation i.e. synchronisation between more than one processes.
- The job of the Producer is to generate the data, put it into the buffer, and again start generating data. While the job of the Consumer is to consume the data from the buffer.
- What’s the problem here?The following are the problems that might occur in the Producer-Consumer:
- The producer should produce data only when the buffer is not full. If the buffer is full, then the producer shouldn’t be allowed to put any data into the buffer.The consumer should consume data only when the buffer is not empty. If the buffer is empty, then the consumer shouldn’t be allowed to take any data from the buffer.The producer and consumer should not access the buffer at the same time.
- We can solve this problem by using semaphores.


<b>Banker’s Algorithm </b>- It is a banker algorithm used to avoid deadlock and allocate resources safely to each process in the computer system. The ‘S-State’ examines all possible tests or activities before deciding whether the allocation should be allowed to each process. It also helps the operating system to successfully share the resources between all the processes. The banker’s algorithm is named because it checks whether a person should be sanctioned a loan amount or not to help the bank system safely simulate allocation resources.


<b>Explain Cache</b>- Cache memory is an extremely fast memory type that acts as a buffer between RAM and the CPU. It holds frequently requested data and instructions so that they are immediately available to the CPU when needed.


<b>Diff between direct mapping and associative mapping </b>

<b>Diff between multitasking and multiprocessing </b>

<b>What is DBMS ? Mention advantages.. </b>- Database Management System (DBMS) is a software for storing and retrieving users’ data while considering appropriate security measures. It consists of a group of programs which manipulate the database. The DBMS accepts the request for data from an application and instructs the operating system to provide the specific data. In large systems, a DBMS helps users and other third-party software to store and retrieve data. Advantages:

- Improved data sharing
- Improved data security
- Better data integration
- Minimised data inconsistency
- Improved data access
- Improved decision making
- Improved end-user productivity


<b>What is Database? </b>- A database is an organised collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just a database.


<b>What is a database system? </b>

<b>What is RDBMS ? Properties.. </b>- A Relational Database Management system (RDBMS) is a database management system that is based on the relational model. It has the following major components: Table, Record/Tuple/Row, Field, and Column/Attribute. Examples of the most popular RDBMS are MYSQL, Oracle, IBM DB2, and Microsoft SQL Server database. Relational databases have the following properties:

- Values are atomic.
- All of the values in a column have the same data type.
- Each row is unique.
- The sequence of columns is insignificant.
- The sequence of rows is insignificant.
- Each column has a unique name.
- Integrity constraints maintain data consistency across multiple tables.


<b>Types of database languages </b>- Data Definition Language: DDL stands for Data Definition Language. It is used to define database structure or pattern.
- Data Manipulation Language: DML stands for Data Manipulation Language. It is used for accessing and manipulating data in a database. It handles user requests.
- Data Control Language: DCL stands for Data Control Language. It is used to retrieve the stored or saved data.
- Transaction Control Language: TCL is used to run the changes made by the DML statement. TCL can be grouped into a logical transaction.


<b>ACID properties (VVVVV IMP) </b>- To ensure the consistency of the database, certain properties are followed by all thetransactions occurring in the system. These properties are called ACID Properties of a transaction.
- Atomicity
- Consistency
- Isolation
- Durability


<b>Difference between vertical and horizontal scaling </b>- Scaling alters the size of a system. In the scaling process, we either compress or expand the system to meet the expected needs. The scaling operation can be achieved by adding resources to meet the smaller expectation in the current system, or by adding a new system in the existing one, or both.
- Vertical scaling keeps your existing infrastructure but adds computing power. Your existing pool of code does not need to change — you simply need to run the same code on machines with better specs. By scaling up, you increase the capacity of a single machine and increase its throughput. Vertical scaling allows data to live on a single node, and scaling spreads the load through CPU and RAM resources for your machines.
- Horizontal scaling simply adds more instances of machines without first implementing improvements to existing specifications. By scaling out, you share the processing power and load balancing across multiple machines.


<b>What is sharding </b>- Sharding is a method of splitting and storing a single logical dataset in multiple databases. By distributing the data among multiple machines, a cluster of database systems can store larger dataset and handle additional requests. Sharding is necessary if a dataset is too large to be stored in a single database. Moreover, many sharding strategies allow additional machines to be added. Sharding allows a database cluster to scale along with its data and traffic growth.

<b>Keys in DBMS </b>- A key is a set of attributes that can identify each tuple uniquely in the given relation.

- Super Key – A superkey is a set of attributes that can identify each tuple uniquely in the given relation. A super key may consist of any number of attributes.
- Candidate Key – A set of minimal attribute(s) that can identify each tuple uniquely in the given relation is called a candidate key.
- Primary Key – A primary key is a candidate key that the database designer selects while designing the database. Primary Keys are unique and NOT NULL.
- Alternate Key – Candidate keys that are left unimplemented or unused after implementing the primary key are called alternate keys.
- Foreign Key – An attribute ‘X’ is called as a foreign key to some other attribute ‘Y’ when its values are dependent on the values of attribute ‘Y’. The relation in which attribute ‘Y’ is present is called the referenced relation. The relation in which attribute ‘X’ is present is called the referencing relation.
- Composite Key – A primary key composed of multiple attributes and not just a single attribute is called a composite key.
- Unique Key – It is unique for all the records of the table. Once assigned, its value cannot be changed i.e. it is non-updatable. It may have a NULL value.


<b>Types of relationship </b>- A relationship is defined as an association among several entities.
- Unary Relationship Set – Unary relationship set is a relationship set where only one entity set participates in a relationship set.
- Binary Relationship Set – Binary relationship set is a relationship set where two entity sets participate in a relationship set.
- Ternary Relationship Set – Ternary relationship set is a relationship set where three entity sets participate in a relationship set.
- N-ary Relationship Set – N-ary relationship set is a relationship set where ‘n’ entity sets participate in a relationship set.


<b>Data abstraction in DBMS, three levels of it </b>- Data Abstraction is a process of hiding unwanted or irrelevant details from the end user. It provides a different view and helps in achieving data independence which is used to enhance the security of data.
- Database systems include complex data-structures. In terms of retrieval of data, reduce complexity in terms of usability of users and in order to make the system efficient, developers use levels of abstraction that hide irrelevant details from the users. Levels of abstraction simplify database design.


<b>Indexing in DBMS </b>- Indexing is a way to optimise the performance of a database by minimising the number of disk accesses required when a query is processed. It is a data structure technique which is used to quickly locate and access the data in a database.


<b>What is DDL (Data Definition Language) </b>- DDL stands for Data Definition Language. It is used to define database structure or pattern.It is used to create schema, tables, indexes, constraints, etc. in the database.Using the DDL statements, you can create the skeleton of the database.Data definition language is used to store the information of metadata like the number of tables and schemas, their names, indexes, columns in each table, constraints, etc.


<b>What is DML (Data Manipulation Language)</b>- DML stands for Data Manipulation Language. It is used for accessing and manipulating data in a database. It handles user requests.


<b>What is normalization ? Types of normalization.</b>- Normalization is the process of organizing data by disintegrating bigger table into smaller one’swith proper dependencies
- Redundant Data wastes a lot of disk space and creates maintenance problems (Update, Insert and Delete Anomaly). Hence the DB tables should be Normalized.
- The process of Normalization is achieved by following some rules which are defined as Normal Forms
- There are basically 3 types of Normal Form – 1NF, 2NF, 3NF. Strictness increases as we go from 1NF to 3NF.
- Apart from the above mentioned Normal Form there exist one more Form called Boyce Codd Normal Form (BCNF) . This is an advanced version of 3NF and is even stricter than 3NF.
- Read normalisation in details


<b>What is denormalization ? </b>- Denormalization is a database optimization technique in which we add redundant data to one or more tables. This can help us avoid costly joins in a relational database. Note that denormalization does not mean not doing normalisation. It is an optimization technique that is applied after doing normalisation.


<b>What is functional dependency ? </b>- A functional dependency is a constraint that specifies the relationship between two sets of attributes where one set can accurately determine the value of other sets. It is denoted as X → Y, where X is a set of attributes that is capable of determining the value of Y. The attribute set on the left side of the arrow, X is called Determinant, while on the right side, Y is called the Dependent.


<b>E-R Model ? </b>- ER model stands for an Entity-Relationship model. It is a high-level data model. This model is used to define the data elements and relationship for a specified system.
- It develops a conceptual design for the database. It also develops a very simple and easy to design view of data.In ER modelling, the database structure is portrayed as a diagram called an entity-relationship diagram.


<b> Conflict Serializability in DBMS .. </b>- Serializability is a concept that helps us to check which schedules are serializable. A serializable schedule is the one that always leaves the database in consistent state.
- A schedule is called conflict serializability if after swapping of non-conflicting operations, it can transform into a serial schedule. The schedule will be a conflict serializable if it is conflict equivalent to a serial schedule.


<b>What is CCP ? (Concurrency Control Protocols) </b>- Concurrency Control is the management procedure that is required for controlling concurrent execution of the operations that take place on a database.
- The concurrency control protocols ensure the atomicity, consistency, isolation, durability and serializability of the concurrent execution of the database transactions.
- Therefore, these protocols are categorised as:
- Lock Based Concurrency Control Protocol
- Timestamp Concurrency Control Protocol
- Validation Based Concurrency Control Protocol


<b>Entity, Entity Type, Entity Set, Weak Entity Set.. </b>- Entity in DBMS can be a real-world object with an existence, For example, in a College database, the entities can be Professor, Students, Courses, etc.
- The entity type is a collection of the entity having similar attributes.
- Types of Entity type:
- Strong Entity Type:Strong entities are those entity types which have a key attribute. The primary key helps in identifying each entity uniquely. It is represented by a rectangle.
- Weak Entity Type: Weak entity type doesn’t have a key attribute. Weak entity types can’t be identified on their own. It depends upon some other strong entity for its distinct identity.
- Entity Set: Entity Set is a collection of entities of the same entity type. We can say that entity type is a superset of the entity set as all the entities are included in the entity type.


<b>What are SQL commands ? Types of them.. </b>- https://www.javatpoint.com/dbms-sql-command


<b>Nested Queries in SQL ? </b>- https://www.tutorialspoint.com/explain-about-nested-queries-in-dbms


<b>What is JOIN .. Explain types of JOINs </b>- https://www.javatpoint.com/dbms-sql-joins


<b>Inner and Outer Join </b>- Here are the different types of the JOINs in SQL:
- (INNER) JOIN:  Returns records that have matching values in both tables
- LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
- RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
- FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table


<b>Diff between 2 tier and 3 tier architecture </b>- https://www.geeksforgeeks.org/difference-between-two-tier-and-three-tier-database-architecture/


<b>Diff between TRUNCATE and DELETE command .. </b>

<b>Difference between Intension and Extension in a DataBase</b>

<b>Difference between share lock and exclusive lock, definition of lock </b>

<b>Define network </b>- A network is a set of devices that are connected with a physical media link. In
- a network, two or more nodes are connected by a physical link or two or more networks are connected by one or more nodes. A network is a collection of devices connected to each other to allow the sharing of data.


<b>What do you mean by network topology, and explain types of them </b>- Network topology is the arrangement of nodes and links of a network.
- Topologies are categorized as either physical network topology or logical network topology.
- The topology of a network is key to determining its performance.
- Network topology can be categorized into – Bus Topology, Ring Topology, Star Topology, Mesh Topology, Tree Topology.
- Read this article for more details.


<b>Define bandwidth, node and link ? </b>- Bandwidth is the data transfer capacity of a computer network in bits per second (Bps). The term may also be used colloquially to indicate a person’s capacity for tasks or deep thoughts at a point in time.
- A network is a connection setup of two or more computers directly connected by some physical mediums like optical fibre or coaxial cable. This physical medium of connection is known as a link, and the computers that it is connected to are known as nodes

<b>Explain TCP model .. </b>- It is a compressed version of the OSI model with only 4 layers. It was developed by the US Department of Defence (DoD) in the 1860s. The name of this model is based on 2 standard protocols used i.e. TCP (Transmission Control Protocol) and IP (Internet Protocol).

1. Network Access/Link layer : Decides which links such as serial lines or classic Ethernet must be used to meet the needs of the connectionless internet layer. Ex – Sonet, Ethernet

2. Internet : The internet layer is the most important layer which holds the whole architecture together. It delivers the IP packets where they are supposed to be delivered. Ex – IP, ICMP.

3. Transport : Its functionality is almost the same as the OSI transport layer. It enables peer entities on the network to carry on a conversation. Ex – TCP, UDP (User Datagram Protocol)

4. Application : It contains all the higher-level protocols. Ex – HTTP, SMTP, RTP,DNS


<b>Layers of OSI model </b>- There are majorly 2 main layers in the OSI model:
-  Physical Layer
- Data Link Layer
- Read this article for details


<b>Significance of Data Link Layer</b>- It is used for transferring the data from one node to another node.
- It receives the data from the network layer and converts the data into data frames and then attaches the physical address to these frames which are sent to the physical layer.
- It enables the error-free transfer of data from one node to another node.
- Functions of Data-link layer:
- Frame synchronisation: Data-link layer converts the data into frames, and it ensures that the destination must recognize the starting and ending of each frame.
- Flow control: Data-link layer controls the data flow within the network.
- Error control: It detects and corrects the error occurred during the transmission from source to destination.
- Addressing: Data-link layers attach the physical address with the data frames so that the individual machines can be easily identified.
- Link management: Data-link layer manages the initiation, maintenance and termination of the link between the source and destination for the effective exchange of data.


<b>Define gateway, difference between gateway and router .. </b>- A node that is connected to two or more networks is commonly known as a gateway. It is also known as a router. It is used to forward messages from one network to another. Both the gateway and router regulate the traffic in the network. Differences between gateway and router: A router sends the data between two similar networks while gateway sends the data between two dissimilar networks.


<b>What does ping command do ? </b>- The “ping” is a utility program that allows you to check the connectivity between the network devices. You can ping devices using its IP address or name.


<b>What is DNS, DNS forwarder, NIC, ? </b>- DNS:
- DNS is an acronym that stands for Domain Name System.DNS was introduced by Paul Mockapetris and Jon Postel in 1983.
- It is a naming system for all the resources over the internet which includes physical nodes and applications. It is used to locate resources easily over a network.
- DNS is an internet which maps the domain names to their associated IP addresses.
- Without DNS, users must know the IP address of the web page that you wanted to access.

**DNS Forwarder** : A forwarder is used with a DNS server when it receives DNS queries that cannot be resolved quickly. So it forwards those requests to external DNS servers for resolution. A DNS server which is configured as a forwarder will behave differently than the DNS server which is not configured as a forwarder. NIC stands for **Network Interface Card**. It is a peripheral card attached to the PC to connect to a network. Every NIC has its own MAC address that identifies the PC on the network. It provides a wireless connection to a local area network. NICs were mainly used in desktop computers.


<b>What is MAC address ? </b>- A media access control address (MAC address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment.


<b>What is IP address, private IP address, public IP address, APIPA ? </b>- An IP address is a unique address that identifies a device on the internet or a local network. IP stands for “Internet Protocol,” which is the set of rules governing the format of data sent via the internet or local network.
- Private IP Address – There are three ranges of IP addresses that have been reserved
- for IP addresses. They are not valid for use on the internet. If you want to access the
- internet on these private IPs, you must use a proxy server or NAT server.
- Public IP Address – A public IP address is an address taken by the Internet Service
- Provider which facilitates communication on the internet.
- APIPA stands for Automatic Private IP Addressing (APIPA). It is a feature or characteristic in operating systems (eg. Windows) which enables computers to self-configure an IP address and subnet mask automatically when their DHCP(Dynamic Host Configuration Protocol:A DHCP Server is a network server that automatically provides and assigns IP addresses, default gateways and other network parameters to client devices. It relies on the standard protocol known as Dynamic Host Configuration Protocol) server isn’t reachable


<b>Difference between IPv4 and IPv6</b>

<b>What is subnet ? </b>- A subnet is a network inside a network achieved by the process called subnetting which helps divide a network into subnets. It is used for getting a higher routing efficiency and enhances the security of the network. It reduces the time to extract the host address from the routing table.


<b>Firewalls </b>- The firewall is a network security system that is used to monitor the incoming
- and outgoing traffic and blocks the same based on the firewall security policies. It acts as a wall between the internet (public network) and the networking devices (a private network). It is either a hardware device, software program, or a combination of both. It adds a layer of security to the network.

<b>Different type of delays </b>- The delays, here, means the time for which the processing of a particular packet takes place.

- Transmission Delay
- Propagation delay
- Queueing delay
- Processing delay


<b>3 way handshaking </b>- Three-Way HandShake or a TCP 3-way handshake is a process which is used in a TCP/IP network to make a connection between the server and client. It is a three-step process that requires both the client and server to exchange synchronisation and acknowledgment packets before the real data communication process starts.
- Three-way handshake process is designed in such a way that both ends help you to initiate, negotiate, and separate TCP socket connections at the same time. It allows you to transfer multiple TCP socket connections in both directions at the same time.


<b>Server-side load balancer</b>- All backend server instances are registered with a central load balancer. A client requests this load balancer which then routes the request to one of the server instances using various algorithms like round-robin. AWS ELB(Elastic Load Balancing) is a prime example of server-side load-balancing that registers multiple EC2 instances launched in its auto-scaling group and then routes the client requests to one of the EC2 instances.
- Advantages of server-side load balancing:
- Simple client configuration: only need to know the load-balancer address.
- Clients can be untrusted: all traffic goes through the load-balancer where it can be looked at. Clients are not aware of the backend servers.


<b>RSA Algorithm </b>- RSA algorithm is an asymmetric cryptography algorithm. Asymmetric actually means that it works on two different keys i.e. Public Key and Private Key. As the name describes, the Public Key is given to everyone and the Private key is kept private.
- An example of asymmetric cryptography : A client (for example browser) sends its public key to the server and requests for some data. The server encrypts the data using the client’s public key and sends the encrypted data. Client receives this data and decrypts it. Since this is asymmetric, nobody else except the browser can decrypt the data even if a third party has the public key of the browser.


<b>What is HTTP and HTTPS protocol ? </b>- HTTP is the HyperText Transfer Protocol which defines the set of rules and standards on how the information can be transmitted on the World Wide Web (WWW). It helps the web browsers and web servers for communication. It is a ‘stateless protocol’ where each command is independent with respect to the previous command. HTTP is an application layer protocol built upon the TCP. It uses port 80 by default. HTTPS is the HyperText Transfer Protocol Secure or Secure HTTP. It is an advanced and a secured version of HTTP. On top of HTTP, SSL/TLS protocol is used to provide security. It enables secure transactions by encrypting the communication and also helps identify network servers securely. It uses port 443 by default.


<b>What is SMTP protocol ? </b>- SMTP is the Simple Mail Transfer Protocol. SMTP sets the rule for communication between servers. This set of rules helps the software to transmit emails over the internet. It supports both End-to-End and Store-and-Forward methods. It is in always-listening mode on port 25.


<b>TCP and UDP protocol, prepare differences</b>- TCP is a connection-oriented protocol, whereas UDP is a connectionless protocol. A key difference between TCP and UDP is speed, as TCP is comparatively slower than UDP. Overall, UDP is a much faster, simpler, and
- efficient protocol, however, retransmission of lost data packets is only possible with TCP.
- TCP provides extensive error checking mechanisms. It is because it provides flow control and acknowledgment of data. UDP has only the basic error checking mechanism using checksums.

<b>What happens when you enter “google.com” (very very famous question) </b>- Check the browser cache first if the content is fresh and present in the cache display the same.

- If not, the browser checks if the IP of the URL is present in the cache (browser and OS) if not then requests the OS to do a DNS lookup using UDP to get the corresponding IP address of the URL from the DNS server to establish a new TCP connection.
- A new TCP connection is set between the browser and the server using three-way handshaking.
- An HTTP request is sent to the server using the TCP connection.
- The web servers running on the Servers handle the incoming HTTP request and send the HTTP response.
- The browser processes the HTTP response sent by the server and may close the TCP connection or reuse the same for future requests.
- If the response data is cacheable then browsers cache the same.
- Browser decodes the response and renders the content.


<b>Hub vs Switch </b>- Hub: Hub is a networking device which is used to transmit the signal to each port
- (except one port) to respond from which the signal was received. Hub is operated on a Physical layer. In this packet filtering is not available. It is of two types: Active Hub, Passive Hub.
- Switch: Switch is a network device which is used to enable the connection
- establishment and connection termination on the basis of need. Switch is operated on the Data link layer. In this packet filtering is available. It is a type of full duplex
- transmission mode and it is also called an efficient bridge


<b>VPN, advantages and disadvantages of it </b>- VPN (Virtual Private Network) : VPN or the Virtual Private Network is a private WAN
- (Wide Area Network) built on the internet. It allows the creation of a secured tunnel
- (protected network) between different networks using the internet (public network). By using the VPN, a client can connect to the organisation’s network remotely.

**Advantages of VPN :**

- VPN is used to connect offices in different geographical locations remotely and is cheaper when compared to WAN connections.
- VPN is used for secure transactions and confidential data transfer between multiple offices located in different geographical locations.
- VPN keeps an organisation’s information secured against any potential threats or intrusions by using virtualization.
- VPN encrypts the internet traffic and disguises the online identity

**Disadvantages of VPN :**

- Not designed for continuous use
- Complexity prevents scalability
- Lack of granular security
- Unpredictable performance
- Unreliable availability

<b>LAN</b>- A local area network (LAN) is a collection of devices connected together in one physical location, such as a building, office, or home. A LAN can be small or large, ranging from a home network with one user to an enterprise network with thousands of users and devices in an office or school.
