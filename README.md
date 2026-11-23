# data-cleaning-oop

**Project Overview.** Raw datasets are loaded into a dataset store and passed through modular cleaning and validation steps before generating a summary report. Missing values can be filled or dropped, text fields can be trimmed and normalized in casing, duplicate records can be removed, and columns and data types can be checked against a schema. Invalid data or failed validation rules raise `DataValidationError`, while pipeline execution failures raise `CleaningError`.

## Installation

Install from PyPI:
pip install data-cleaning-oop

For local development:
git clone https://github.com/lynx-182007/data-cleaning-oop.git
cd data-cleaning-oop
pip install -e .

## Usage

python main.py
python -m unittest discover tests

## Contributors

| Module | Owner | Contract ABC / Exception it implements |
|---|---|---|
| dataset | EDURIA | `IDataSet`, `DataValidationError` |
| missing_handler | MACARANAS | `IMissingValueHandler` |
| text_normalizer | KATIPUNAN | `ITextNormalizer` |
| duplicate_remover & schema_validator | LINGCONG | `IDuplicateRemover`, `ISchemaValidator`, `DataValidationError` |
| pipeline & report | UBSUBAN | `ICleaningPipeline`, `ICleaningReport`, `CleaningError` |

## Workflow & Commits

- Develop features on separate `feature/<module>` branches and merge into `main` via Pull Requests (requiring 1 approval and resolved review comments).
- Maintain a clear and consistent commit history using `<type>(<scope>): <summary>` (e.g., `feat(dataset): implement IDataSet storage methods`, `fix(validator): raise DataValidationError on type mismatch`).

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.