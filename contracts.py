from abc import ABC, abstractmethod


class CleaningError(Exception):
    """Raised when a cleaning or pipeline rule fails."""


class DataValidationError(Exception):
    """Raised when dataset columns, types, or values are invalid."""


class IDataSet(ABC):
    """Contract for dataset storage: what other modules may read or update."""

    @property
    @abstractmethod
    def data(self):
        """List of row records stored in the dataset."""

    @abstractmethod
    def load_data(self, data):
        """Load initial records into the dataset.
        Raises DataValidationError if data format is invalid."""

    @abstractmethod
    def get_data(self):
        """Return current dataset records."""

    @abstractmethod
    def update_data(self, data):
        """Replace stored records with updated data.
        Raises DataValidationError if data format is invalid."""


class IMissingValueHandler(ABC):
    """Contract for handling missing values in a dataset."""

    @abstractmethod
    def fill_missing(self, data, value):
        """Replace missing entries using value and return updated records."""

    @abstractmethod
    def drop_missing(self, data):
        """Remove records with missing values and return remaining records."""


class ITextNormalizer(ABC):
    """Contract for normalizing text strings."""

    @abstractmethod
    def trim_whitespace(self, text):
        """Trim extra whitespace from text and return cleaned string."""

    @abstractmethod
    def change_case(self, text):
        """Adjust text casing and return updated string."""

    @abstractmethod
    def normalize_text(self, text):
        """Normalize text by trimming whitespace and applying casing."""


class IDuplicateRemover(ABC):
    """Contract for removing duplicate records from a dataset."""

    @abstractmethod
    def remove_duplicates(self, data):
        """Remove duplicate records and return unique records."""


class ISchemaValidator(ABC):
    """Contract for validating dataset columns and value types."""

    @abstractmethod
    def validate_columns(self, data, schema):
        """True if records match expected columns in schema.
        Raises DataValidationError on column mismatch."""

    @abstractmethod
    def validate_types(self, data, schema):
        """True if record values match expected types in schema.
        Raises DataValidationError on type mismatch."""


class ICleaningReport(ABC):
    """Contract for storing and displaying the cleaning summary report."""

    @property
    @abstractmethod
    def summary(self):
        """Formatted summary string of cleaning results."""

    @abstractmethod
    def generate_report(self):
        """Build and store the summary report."""

    @abstractmethod
    def display_report(self):
        """Display the generated summary report."""


class ICleaningPipeline(ABC):
    """Contract for running the cleaning steps and generating a report."""

    @property
    @abstractmethod
    def dataset(self):
        """Dataset instance managed by the pipeline."""

    @abstractmethod
    def clean_data(self):
        """Run cleaning and validation steps over the dataset.
        Raises CleaningError if pipeline execution fails."""

    @abstractmethod
    def run_pipeline(self):
        """Execute clean_data() and display the report."""