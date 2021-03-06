# Development Documentation

## Class Diagram

![Class Diagrm](img/yed/class_diagram.png)

## Program Flow

<img src="img/yed/screens.png" width="200">

1. The `__main__()` function initiate an `app`.

1. `app` initiates `controller`.

1. `controller` initiates `model` and adds itself as the model's `controller`.

1. `controller` initiates `view` and adds itself as the view's `controller`.

1. `view` initiates `welcome_win`.

1. `controller` calls `view_show_welcome_win`.

1. `controller` calls `view.event_loop()`.

From here out the program's behavior is dictated by the event that occurs. Events are caught by the `view` which calls a function in the `controller`. The `controller` manipulates the `model` as required. It refreshes the `view` after any change to the model, such as loading it from disk, saving it, or changing a property.

## Documentation Color Pallette

<https://flatuicolors.com/palette/us>

## Requirements

### Non-Functional

- [ ] User manual.
- [ ] Type hints and type-checking.
- [ ] SQLite for application file format.
- [ ] ZODB for storage.
- [ ] 100 code coverage testing.
- [ ] Config stored in environment variables.
- [ ] Config isolated from code.
- [ ] Dependencies vendored-in.

### Functional

- [ ] Save to a file.
- [ ] Save As function.
- [ ] Open a file.
- [ ] User settings.
- [ ] Infinite undo/redo.

## File Handling

[ZODB](https://zodb-docs.readthedocs.io/en/latest/) is used for file storage. This has some nice side-effects:

- Extremely clean code. Use ordinary Python classes derived from `persistent.Persistent`.
- Undo capabilities. TODO: Research how to do this.
- [ACID](<https://en.wikipedia.org/wiki/ACID_(computer_science)>) transaction protect data integrity.

## Testing

[Coverage 5.2.1](https://coverage.readthedocs.io/en/coverage-5.2.1/) and Python 3.8.5 `unittest` are used for testing.

```zsh
# Run tests
$ make test

# Run tests and open browser to see Coverage HTML results
$ make coverage
```

# Static Type Checking

It seems like a good idea to do some static tape checking for quality control purposes. Here is a list of a few options to choose from.

- [mypy](http://mypy-lang.org)
