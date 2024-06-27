from itertools import repeat


class RecursiveAutoPrefetchManagerMixin:
    """
    Manager mixin to allow a model with a recursive field to be automatically prefetched at a given depth.
    """
    depth: int
    lookup_field: str

    def get_queryset(self):
        if not self.depth or not self.lookup_field:
            raise NotImplementedError("Mixin attribute is missing")
        lookup = '__'.join(repeat(self.lookup_field, self.depth))
        return super().get_queryset().prefetch_related(lookup)
