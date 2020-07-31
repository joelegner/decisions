# Development Documentation

## Class Diagram

![Class Diagram](img/yed/class_diagram.png)

## Program Flow

<img src="img/yed/screens.png" width="200">

## Program Start

1. Initiate `app`.

1. `app` initiates `controller`.

1. `controller` initiates `model` and adds itself as the model's `controller`.

1. `controller` initiates `view` and adds itself as the view's `controller`.

1. `view` initiates `welcome_win`.

1. `controller` calls `view_show_welcome_win`.

1. `controller` calls `view.event_loop()`.

From here out the program's behavior is dictated by the event that occurs. Events are caught by the `view` which calls a function in the `controller`. The `controller` manipulates the `model` as required. It refreshes the `view` after any change to the model, such as loading it from disk, saving it, or changing a property.
