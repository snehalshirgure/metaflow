from metaflow.decorators import StepDecorator


class PodAnnotationDecorator(StepDecorator):
    """
    Add a single pod annotation. This decorator can be used multiple time per step.
    Repeated adding assigning value under same name will overwrite previous value.
    """

    name = "pod_annotation"
    defaults = {
        "name": None,
        "value": None,
    }


class PodLabelDecorator(StepDecorator):
    """
    Add a single pod label. This decorator can be used multiple time per step.
    Repeated adding assigning value under same name will overwrite previous value.
    """

    name = "pod_label"
    defaults = {
        "name": None,
        "value": None,
    }
