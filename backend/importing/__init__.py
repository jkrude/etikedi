from pathlib import Path

from .cifar import convert_cifar
from .dwtc import convert_dwtc
from .generic import import_dataset
from .religious_texts import convert_religions_texts
from ..models import Dataset
from ..config import db

DATA_PATH = (Path(__file__).absolute() / "../../data").resolve()


def import_test_datasets():
    if db.query(Dataset).count():
        return
    DATA_PATH.mkdir(parents=True, exist_ok=True)
    convert_cifar(DATA_PATH)
    convert_dwtc(DATA_PATH)
    convert_religions_texts(DATA_PATH)


if __name__ == "__main__":
    import_test_datasets()
