# Copyright (c) Facebook, Inc. and its affiliates.
from pythia.common.registry import registry
from pythia.tasks.vqa.vqa2 import VQA2Builder

from .dataset import VizWizDataset


@registry.register_builder("vizwiz")
class VizWizBuilder(VQA2Builder):
    def __init__(self):
        super().__init__()
        self.dataset_name = "vizwiz"
        self.set_dataset_class(VizWizDataset)

    def update_registry_for_model(self, config):
        super().update_registry_for_model(config)
