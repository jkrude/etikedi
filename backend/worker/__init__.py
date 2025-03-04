from sqlalchemy import func as db_functions

from .prepare import *
from .manager import manager
from ..config import logger, db
from ..models import Dataset, Sample
from ..utils import number_of_labelled_samples


# def should_label_random_sample(dataset: Dataset, random_sample_every: int = 10) -> bool:
#     # Could possibly fix https://gitlab.hrz.tu-chemnitz.de/ddsg/aergia/aergia/-/issues/62
#     # Used when active learning code is not used at all to speed up development of frontend
#     # In this case, we can skip the count query
#     if random_sample_every == 1:
#         return True
#
#     return number_of_labelled_samples(dataset) % random_sample_every == 0
#
#
# def get_random_unlabelled_sample(dataset: Dataset) -> Sample:
#     return (
#         db.query(Sample).filter(Sample.dataset == dataset, ~Sample.associations.any())
#         .order_by(db_functions.random())
#         .first()
#     )


# def get_next_sample(dataset: Dataset) -> Sample:
#     config = dataset.get_config()
#     if should_label_random_sample(dataset=dataset, random_sample_every=config.RANDOM_SAMPLE_EVERY):
#         logger.info("Label random sample")
#         return get_random_unlabelled_sample(dataset)
#
#     # Retrieve pipe endpoint from process manager
#     process_resources = manager.get_or_else_load(dataset)
#     pipe_endpoint = process_resources.pipe
#
#     if pipe_endpoint.poll(config.TIMEOUT_FOR_WORKER):
#         logger.info("Found new data points")
#         next_sample_id = pipe_endpoint.recv()
#         return db.query(Sample).get(next_sample_id)
#     else:
#         # Send back a random label anyway for testing purposes
#         logger.info(
#             "No samples available from AL, send back a random sample instead"
#         )
#         return get_random_unlabelled_sample(dataset)
#
#
# def notify_about_new_sample(
#     dataset: Dataset, user_id: int, sample_id: int, label_id: int
# ) -> None:
#     if dataset.get_config().RANDOM_SAMPLE_EVERY == 1:
#         return
#
#     process_resources = manager.get_or_else_load(dataset=dataset)
#     pipe_endpoint = process_resources["pipe"]
#     pipe_endpoint.send({"id": sample_id, "label": label_id, "user": user_id})
