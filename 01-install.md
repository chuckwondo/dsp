# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

### Install [Homebrew](http://brew.sh/) on Mac

If you use a Mac, install Homebrew if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.


### Q1. Python Version 2 or 3

Did you install Python 2 or 3? Why?  

> I installed Anaconda with Python 2.7 since Python 2 is more commonly used than Python 3.
>
> To check the version of Python installed, run the following command:
>
>     $ python --version
>     Python 2.7.10 :: Anaconda 2.3.0 (x86_64)
>
> However, I also created a separate environment with Python 3.4, including all of the same packages installed in the default environment, by running the following command:
>
>     conda create -n py34 python=3.4 anaconda
>
> I can switch to the new environment by using the following command:
>
>     source activate py34
>
> I can then confirm that the correct version of Python is installed in the new environment:
>
>     $ python --version
>     Python 3.4.3 :: Anaconda 2.3.0 (x86_64)
>
> Finally, I can restore the default environment by deactivating the new environment:
>
>     source deactivate

### Q2. Which Python Version Installed

How can you check the version of Python installed if you happen to be on an unfamiliar computer?

>     python --version
>     python -V
