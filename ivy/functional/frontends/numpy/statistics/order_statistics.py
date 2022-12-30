# global
import ivy.functional.frontends.numpy
from ivy.functional.frontends.numpy import from_zero_dim_arrays_to_scalar
from ivy.functional.frontends.numpy.func_wrapper import (
    to_ivy_arrays_and_back,
)


@to_ivy_arrays_and_back
@from_zero_dim_arrays_to_scalar
def percentile(a,
               q,
               /,
               *,
               axis=None,
               out=None,
               overwrite_input=False,
               method="linear",
               keepdims=False,
               interpolation=None):

    # The only difference between the quantile and percentile
    # formula it's that quantile has the 'q' in range 0 to 1
    # and percentile has the 'q' from 0 to 100.
    # Here it's used the ivy.quantile due to the fact that ivy.percentile
    # doesn't exist, so in order to calculate the percentile,
    # the line below converts ivy.quantile to percentile.
    q /= 100

    axis = tuple(axis) if isinstance(axis, list) else axis

    ret = ivy.quantile(a, q, axis=axis, keepdims=keepdims, out=out,
                       interpolation=interpolation)

    return ret
