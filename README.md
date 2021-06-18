Hello World - Docker Demo
=========================

This repository contains the code and configuration file for a **Hello World** example that defines five workflow operators that are executed using Docker containers. These operators can be registered and run with an experimental version of the [drama workflow engine](https://github.com/heikomuller/drama/tree/feature/docker).


Try it out
----------

**Register**: The operators that are defined in this repository need to be registered (installed) with the local drama instance. Use the following command to register the operators directly from this GitHub repository:

```
drama register -s https://github.com/heikomuller/docker-helloworld-example.git
```

 After registration, the operators can be used in workflow definitions like any other drama workflow operator. The module for the task request execute function is `drama.core.docker.exec`.

**Run**: Use the example script [run_hello_world.py](https://github.com/heikomuller/drama/blob/feature/docker/examples/docker/run_hello_world.py) to run a three-step workflow that (i) downloads a names file, (ii) takes a random sample from that file, and (iii) outputs a greeting phrase for each name in the sample.

The following command will select a sample of size 5 (using a random state seed of 42) and write a greeting phrase *Hey there <name>!* for each name.

```drive
python examples/docker/run_hello_world.py -g "Hey there" -s 5 -r 42
```

After a successful run, files that are stored in the global data catalog and in the folder for the workflow run.
