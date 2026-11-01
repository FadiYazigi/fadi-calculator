from decimal import Decimal, InvalidOperation
from pathlib import Path
import sys

import webview


class CalculatorAPI:
    """Python calculation engine exposed to the HTML interface."""

    @staticmethod
    def _format_result(value: Decimal) -> str:
        if not value.is_finite():
            raise ValueError("The result is outside the supported range.")

        # Avoid displaying unnecessary trailing zeros.
        text = format(value, "f")
        if "." in text:
            text = text.rstrip("0").rstrip(".")
        if text in ("", "-0"):
            text = "0"
        return text

    def calculate(self, left, right, operator):
        """Calculate two decimal values and return a JSON-friendly result."""
        try:
            if not isinstance(left, str) or not isinstance(right, str):
                return {"ok": False, "error": "Please enter valid numbers."}

            if len(left) > 100 or len(right) > 100:
                return {"ok": False, "error": "The entered number is too long."}

            a = Decimal(left)
            b = Decimal(right)

            if not a.is_finite() or not b.is_finite():
                return {"ok": False, "error": "Please enter finite numbers."}

            if operator == "+":
                result = a + b
            elif operator == "-":
                result = a - b
            elif operator == "*":
                result = a * b
            elif operator == "/":
                if b == 0:
                    return {
                        "ok": False,
                        "error": "Cannot divide by zero."
                    }
                result = a / b
            else:
                return {"ok": False, "error": "Unsupported operation."}

            return {"ok": True, "result": self._format_result(result)}

        except (InvalidOperation, ValueError, OverflowError):
            return {"ok": False, "error": "Invalid calculation. Please try again."}
        except Exception:
            return {"ok": False, "error": "An unexpected calculation error occurred."}


def resource_path(filename: str) -> Path:
    """Find a bundled resource in development and in a PyInstaller build."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        root = Path(sys._MEIPASS)
    else:
        root = Path(__file__).resolve().parent
    return root / filename


def main():
    html_file = resource_path("index.html")

    if not html_file.is_file():
        raise FileNotFoundError(
            f"Could not find {html_file}. Keep index.html beside calculator.py "
            "and include it when building the EXE."
        )

    html_content = html_file.read_text(encoding="utf-8")

    webview.create_window(
        title="Fadi Calculator 2.0",
        html=html_content,
        js_api=CalculatorAPI(),
        width=410,
        height=690,
        min_size=(370, 620),
        resizable=True,
        background_color="#edf4fd",
        text_select=False,
    )

    # Windows uses Edge WebView2 when its runtime is installed.
    webview.start(gui="edgechromium", debug=False)


if __name__ == "__main__":
    main()
