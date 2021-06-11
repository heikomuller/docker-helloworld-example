Hello World - Docker Demo
=========================

This repository contains the code and configuration file for a **Hello World** example that defines three workflow operators for registration with an experimental version of the [drama workflow engine](https://github.com/heikomuller/drama/tree/feature/docker) that uses Docker to execute serial workflows.


Try it out
----------

Use the example script [install_and_run_from_github.py](https://github.com/heikomuller/drama/blob/feature/docker/examples/docker/install_and_run_from_github.py) to run a workflow containing all operators that are defined in this repository.

The following command will select a sample of size 5 (using a random state seed of 42) and write a greeting phrase *Hey there <name>!* for each name. Uses `/tmp/drama-docker` as the base folder:

```
python examples/docker/install_and_run_from_github.py -g "Hey there" -s 5 -r 42 -o /tmp/drama-docker
```

After a successful run, files that are stored in the global data catalog are in `/tmp/drama-docker/store/`, and workflow run files are in `/tmp/drama-docker/run/`. The resulting greeting file `/tmp/drama-docker/run/greetings.txt` should look like this:

```
Hey there Calva!
Hey there Hicks!
Hey there Newbold!
Hey there Orpah!
Hey there Veradi!
```
