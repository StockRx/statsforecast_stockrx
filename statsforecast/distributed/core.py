# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/distributed.core.ipynb.

# %% auto 0
__all__ = ['ParallelBackend']

# %% ../../nbs/distributed.core.ipynb 4
from typing import Any

from ..core import _StatsForecast

# %% ../../nbs/distributed.core.ipynb 5
class ParallelBackend:
    def forecast(self, df, models, freq, fallback_model=None, **kwargs: Any) -> Any:
        model = _StatsForecast(df=df, models=models, freq=freq, fallback_model=fallback_model)
        return model.forecast(**kwargs)

    def cross_validation(self, df, models, freq, fallback_model=None, **kwargs: Any) -> Any:
        model = _StatsForecast(df=df, models=models, freq=freq, fallback_model=fallback_model)
        return model.cross_validation(**kwargs)
