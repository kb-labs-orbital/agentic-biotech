import pytest
from pathlib import Path
#from biotech.llm.loader import loader
from llama_cpp import Llama
from biotech.llm.loader import load_model

def test_model_path_exists():
    """Ensure default model path resolves correctly."""
    model = load_model()
    assert isinstance(model, Llama)
    # Optionally: check path is the expected default
    path = Path(model.model_path)
    assert path.exists()
    assert path.name.endswith(".gguf")
