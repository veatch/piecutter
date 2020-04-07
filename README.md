# piecutter

Piecutter is a library to add a Python configuration layer on top of
[cookiecutter](https://github.com/cookiecutter/cookiecutter/). Piecutter allows
for more complex behavior while prompting the user during project creation.
Piecutter uses cookiecutter under the hood to generate new projects.

Where cookiecutter uses a `cookiecutter.json` file for template configuration,
for example:

```
{
    "project_name": "My Project",
    "repo_name": "my-repo",
}
```
piecutter uses a `piecutter_config.py` file that defines a `prompt_config`
function:

```
def prompt_config():
    return [
        {'name': 'project_name', 'prompt_type': 'text', 'default_value': 'My Project'},
        {'name': 'repo_name', 'prompt_type': 'text', 'default_value': 'my-repo'},
    ]
```

## Using piecutter

To convert an existing `cookiecutter.json` file to a `piecutter_config.py`
file, piecutter will have a script that will be used like:

```
cookiecutter_to_piecutter.py ~/my_proj/cookiecutter.json -o ~/my_proj/piecutter_config.py
```


## Developing piecutter

Piecutter is intended to be a lightweight library built on top of
[cookiecutter](https://github.com/cookiecutter/cookiecutter/). Piecutter's
project structure mirrors cookiecutter as much as possible. Ideally, piecutter
will not require additional libraries beyond those already required by
cookiecutter. Piecutter only supports Python 3.5+.

## Future improvements

Piecutter will support the following config options:

    - a `description` option to provide a more verbose description of a field.
    - a `clean_field_fn` option to specify a function that validates and cleans
      user input and returns the cleaned value.
    - a `should_prompt_fn` option to specify a function that uses existing
      context to determine whether to prompt for a field (for example, only
      prompt for field B if the value for field A was X).

Using these options would look something like this:

```
def prompt_config():
    return [
        {
            'name': 'repo_name', 'prompt_type': 'text', 'default_value': 'my-repo',
            'description': 'The name of your repository. For more info on how to name your repo, see http:// ...',
            'clean_field_fn': clean_repo_name,
            'should_prompt_fn': should_prompt_repo_name,
        },
    ]


def clean_repo_name(context):
    pass  # Function to validate, clean and return repo_name.


def should_prompt_repo_name(context):
    pass  # Use `context` to determine whether to prompt for repo_name field.
```
