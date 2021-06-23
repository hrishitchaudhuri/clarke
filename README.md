# clarke
clarke is an explicit state model checker for evaluating CTL formulae. 

It is based on Clarke's explicit state model-checking algorithm, and works by testing a CTL formula against a loaded Kripke structure. 
A sample Kripke structure has been provided in `model_checker\main.py`.

To run the model checker, run `python3 bf_compiler/parser.py` and ensure you've loaded the correct Kripke structure in the `parser.py` file. This is largely a personal project, and therefore there might be bugs and many awkward things going on, so feel free to open an issue as necessary.
