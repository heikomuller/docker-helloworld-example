Hello World - Docker Demo
=========================

This repository contains the code and configuration file for a **Hello World** example that defines five workflow operators for registration with an experimental version of the [drama workflow engine](https://github.com/heikomuller/drama/tree/feature/docker) that uses Docker to execute serial workflows.


Try it out
----------

**Register**: The operators that are defined in this repository need to be registered (installed) in the local drama instance before they can be used within a workflow. Use the following command to register the operators directly from this GitHub repository:

```
drama register -s https://github.com/heikomuller/docker-helloworld-example.git
```

**Run**: Use the example script [run_hello_world.py](https://github.com/heikomuller/drama/blob/feature/docker/examples/docker/run_hello_world.py) to run a three-step workflow that (i) downloads a names file, (ii) takes a random sample from that file, and (iii) outputs a greeting phrase for each name in the sample.

The following command will select a sample of size 5 (using a random state seed of 42) and write a greeting phrase *Hey there <name>!* for each name.

```
python examples/docker/run_hello_world.py -g "Hey there" -s 5 -r 42
```

After a successful run, files that are stored in the global data catalog and in the folder for the workflow run.
