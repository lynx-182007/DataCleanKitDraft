import string
from typing import Iterable, List, Optional
from contracts import DataValidationError, ITextNormalizer


class TextNormalizer(ITextNormalizer):
    """Concrete ITextNormalizer supporting whitespace trimming and case conversion."""

    def __init__(self, case_mode: str = "lower") -> None:
        valid_modes = {"lower", "upper", "title", "none"}
        if case_mode not in valid_modes:
            raise DataValidationError(
                f"Invalid case_mode '{case_mode}'. Expected one of {sorted(valid_modes)}."
            )
        self._case_mode = case_mode

    @property
    def case_mode(self) -> str:
        return self._case_mode

    def _validate_text(self, text: str) -> str:
        if not isinstance(text, str):
            raise DataValidationError(f"Expected str, got {type(text).__name__}.")
        return text

    def trim_whitespace(self, text: str) -> str:
        """Trim leading/trailing whitespace and collapse internal whitespace runs."""
        cleaned = self._validate_text(text)
        return " ".join(cleaned.split())

    def change_case(self, text: str) -> str:
        """Adjust text casing according to the configured case_mode."""
        cleaned = self._validate_text(text)
        if self._case_mode == "lower":
            return cleaned.lower()
        if self._case_mode == "upper":
            return cleaned.upper()
        if self._case_mode == "title":
            return cleaned.title()
        return cleaned

    def normalize_text(self, text: str) -> str:
        """Normalize text by trimming whitespace and applying configured casing."""
        trimmed = self.trim_whitespace(text)
        return self.change_case(trimmed)


class PunctuationTextNormalizer(TextNormalizer):
    """Extends TextNormalizer by stripping punctuation characters."""

    def __init__(
        self,
        case_mode: str = "lower",
        punctuation_chars: Optional[str] = None,
    ) -> None:
        super().__init__(case_mode=case_mode)
        chars = punctuation_chars if punctuation_chars is not None else string.punctuation
        self._punctuation_chars = chars
        self._translator = str.maketrans("", "", chars)

    def normalize_text(self, text: str) -> str:
        """Trim whitespace, remove punctuation, collapse spaces, and apply casing."""
        trimmed = self.trim_whitespace(text)
        without_punct = trimmed.translate(self._translator)
        collapsed = " ".join(without_punct.split())
        return self.change_case(collapsed)


class TextNormalizerBatch:
    """Applies an ITextNormalizer across an iterable of text values."""

    def __init__(self, normalizer: Optional[ITextNormalizer] = None) -> None:
        self._normalizer: ITextNormalizer = (
            normalizer if normalizer is not None else TextNormalizer()
        )

    @property
    def normalizer(self) -> ITextNormalizer:
        return self._normalizer

    def normalize_many(self, texts: Iterable[str]) -> List[str]:
        return [self._normalizer.normalize_text(item) for item in texts]