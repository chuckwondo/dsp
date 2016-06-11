## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

> Strictly speaking, there are 9 different degrees, but one of them is `0`, so there are only 8 sensible values. Here are the frequencies of all 9:
>
>     [('0', 1), ('BSEd', 1), ('JD', 1), ('MA', 1), ('MD', 1), ('MPH', 2), ('MS', 2), ('PhD', 31), ('ScD', 6)]

####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

> There are 3 distinct titles:
>
> 1. Assistant Professor of Biostatistics, 12
> 1. Associate Professor of Biostatistics, 12
> 1. Professor of Biostatistics, 13


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>     alisaste@mail.med.upenn.edu
>     atroxel@mail.med.upenn.edu
>     bcfrench@mail.med.upenn.edu
>     bellamys@mail.med.upenn.edu
>     bryanma@upenn.edu
>     dxie@upenn.edu
>     hongzhe@upenn.edu
>     hshou@mail.med.upenn.edu
>     hsu9@mail.med.upenn.edu
>     jaroy@mail.med.upenn.edu
>     jellenbe@mail.med.upenn.edu
>     jinboche@upenn.edu
>     jrlandis@mail.med.upenn.edu
>     jshults@mail.med.upenn.edu
>     knashawn@mail.med.upenn.edu
>     liy3@email.chop.edu
>     michross@upenn.edu
>     mingyao@mail.med.upenn.edu
>     mjoffe@mail.med.upenn.edu
>     mputt@mail.med.upenn.edu
>     msammel@cceb.med.upenn.edu
>     nanditam@mail.med.upenn.edu
>     pgimotty@upenn.edu
>     propert@mail.med.upenn.edu
>     rhubb@mail.med.upenn.edu
>     rlocalio@upenn.edu
>     rshi@mail.med.upenn.edu
>     ruifeng@upenn.edu
>     rxiao@mail.med.upenn.edu
>     sellenbe@upenn.edu
>     shawp@upenn.edu
>     sratclif@upenn.edu
>     sxie@mail.med.upenn.edu
>     warren@upenn.edu
>     weiyang@mail.med.upenn.edu
>     wguo@mail.med.upenn.edu
>     whwang@mail.med.upenn.edu


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

> There are 4 unique email domains:
>
> 1. cceb.med.upenn.edu, 1
> 1. email.chop.edu, 1
> 1. mail.med.upenn.edu, 23
> 1. upenn.edu, 12

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>     >>> print(faculty_dict.items()[:3])
>     [
>     ('Putt', [['PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu']])
>     ('Feng', [['Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu']])
>     ('Bilker', [['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']])
>     ]


####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>     >>> print(prof_dict.items()[:3])
>     [
>     (('Yimei', 'Li'), ['Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu']),
>     (('Hongzhe', 'Li'), ['Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu']),
>     (('Justine', 'Shults'), ['Ph.D.', 'Professor of Biostatistics', 'jshults@mail.med.upenn.edu'])
>     ]

####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>     >>> print(sorted(prof_dict.items(), key=lambda t: t[0][1])[:3])
>     [
>     (('Scarlett', 'Bellamy'), ['Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']),
>     (('Warren', 'Bilker'), ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']),
>     (('Matthew', 'Bryan'), ['PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu'])
>     ]

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

For input, I downloaded "Siddharta" by Herman Hesse from The Gutenburg Project,
and I trimmed everything from the beginning and end that is not part of the main
text. Further, I removed the chapter headings.

To make the output a bit more sensible, I enhanced the general logic as follows:

1. I randomly choose a starting n-gram until I find one that ends a sentence. This ensures the *first word* generated is a word that *starts a sentence*.
1. I generate at least as many words as specified by the user, until the current n-gram ends a sentence. This ensures that the *last word* generated is a word that *ends a sentence*, but at the price of generating more than the desired number of words before stopping.

Usage:

```
$ ./markov.py
Usage: ./markov.py file max_words [ngram_size]
```

Sample run:

```
$ ./markov.py siddhartha.txt 100 3
They listened. Softly sounded the river, singing in many voices. Siddhartha
looked into his eyes. She spoke with a heavy tongue, paralysed by the poison.
"You've become old, my dear," she said, "you've become gray. But you are like
the young Samana, who at one time said to me, you would not walk the path of
the teachings, of the examples, of the repetitions, brightly and quietly his
voice hovered over the listeners, like a light, like a starry sky. When the
Buddha--night had already fallen--ended his speech, many a pilgrim stepped
forward and spoke: "I also take my refuge in his teachings."
```
