
import pandas as pd


class DataSet:
    """Manages datasets for data cleaning operations."""

    def __init__(self, data=None):
        """Initialize the dataset."""
        self._data = data.copy() if data is not None else pd.DataFrame()

    @property
    def data(self):
        """Return a copy of the dataset."""
        return self._data.copy()

    def load(self, file_path):
        """Load a CSV file."""
        self._data = pd.read_csv(file_path)
        return self

    def show(self, rows=5):
        """Display the first rows of the dataset."""
        return self._data.head(rows)

    def get_info(self):
        """Return information about the dataset."""
        return {
            "rows": len(self._data),
            "columns": list(self._data.columns),
            "missing_values": int(self._data.isna().sum().sum()),
            "duplicates": int(self._data.duplicated().sum())
        }

    def get_shape(self):
        """Return the number of rows and columns."""
        return self._data.shape

    def save(self, file_path):
        """Save the dataset as a CSV file."""
        self._data.to_csv(file_path, index=False)

    def __len__(self):
        """Return the number of rows."""
        return len(self._data)

    def __repr__(self):
        """Return a readable dataset description."""
        return (
            f"DataSet(rows={len(self._data)}, "
            f"columns={len(self._data.columns)})"
        )

    def __eq__(self, other):
        """Compare two datasets."""
        if not isinstance(other, DataSet):
            return NotImplemented
        return self._data.equals(other._data)

