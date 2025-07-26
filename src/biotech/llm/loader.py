from pathlib import Path
from llama_cpp import Llama

_DEFAULT_MODEL = (
    Path(__file__).resolve().parents[3]  # project root
    / "models"
    / "BioMistral-7B"
    / "BioMistral-7B.Q4_K_M.gguf"
)

def load_model(model_path: str | Path = _DEFAULT_MODEL) -> Llama:
    """
    Load a GGUF model with llama-cpp and return the Llama instance.
    """
    model_path = Path(model_path).expanduser().resolve()
    return Llama(model_path=str(model_path))

