## What does it do

Generates the code I use to pass parameters to a program or script. It takes the format from a jinja2 template and from a variable .yaml where you specify the arguments.

Usage example:

```
cat param.yaml | ./generate python_jinja2.j2 > test.py 
```

## Variables

You can create a yaml file with the following structure:

* `script_name`. The name of your script
* `script_description`. Description of your script.
* `arguments`. Array of the followin variables:
  * `name`. Name of the argument. Example `server`.
  * `short`. Short name of the argument. Example `s`. 
  * `description`. Description of the argument
  * `mandatory`. True or false depending on if it's mandatory.
  * `default`. Default value for the parameter. Ignored if mandatory flag is also set.
  * `param`. Whether is a parameter or an option. If it's an option, it can be only true or false.

Remember arguments can be divided in two types: options and parameters. Parameters usually include extra information (ie `-s server.gotes.org` where options are interpreted as booleans (ie `-h` for help, `-v` for verbose etc.).

## Template

Now only in python but can be ported in every language.
