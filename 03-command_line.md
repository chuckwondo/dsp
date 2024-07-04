# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

### Q1.  Cheat Sheet of Commands

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> I've been using Linux for years, so I'm already very familiar with everything covered in the Command Line Crash Course. I don't have a need for a cheat sheet here.

### Q2.  List Files in Unix

What do the following commands do:

`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> * `ls` lists the names of the entries in the current directory
> * `ls -a` shows _all_ directory entries, including those that start with a dot (`.`), which are otherwise not shown
> * `ls -l` lists contents in _long_ format, where in addition to names, permissions, sizes, owners, and modified dates are listed as well
> * `ls -lh` is the same as `ls -l` except that file sizes are shown in a more compact notation in units of Bytes, Kilobytes, Megabytes, etc.
> * `ls -lah` is a combination of `ls -a` and `ls -lh`
> * `ls -t` lists contents in order of last-modified time, with the
most-recently modified item listed first
> * `ls -Glp` behaves like `ls -l`, but also uses colors (`G`) to distinguish
 file types and attributes, and adds a trailing slash (`p`) to each directory

### Q3.  More List Files in Unix

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> My favorites are `l`, `a`, `G`, `p`, and `h`

### Q4.  Xargs

What does `xargs` do? Give an example of how to use it.

> The `xargs` utility reads space, tab, newline and end-of-file delimited strings from the standard input and executes a utility with the strings as arguments.
>
> Any arguments specified on the command line are given to the utility upon each invocation, followed by some number of the arguments read from the standard input of `xargs`.  The utility is repeatedly executed until standard input is exhausted.
>
> The following example finds all of the markdown files recursively starting in the current working directory and passes all of them as arguments to the `grep` command following the arguments specified explicity after the `grep` command.
>
> In this case, it results in identifying all of the locations in all of the markdown files where `replace this text with your response` (ignoring case) appears, thus indicating how much pre-work I have left to do.
>
>     find . -name "*.md" | xargs grep -i "replace this text with your response"
