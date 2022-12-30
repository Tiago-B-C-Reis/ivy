# global
from hypothesis import strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
import ivy_tests.test_ivy.test_frontends.test_numpy.helpers as np_frontend_helpers
from ivy_tests.test_ivy.helpers import handle_frontend_test


@handle_frontend_test(
    fn_tree="numpy.quantile",
    dtype_and_a=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("numeric")
    ),
    dtype_and_q=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("numeric")
    ),
    keep_dims=st.booleans(),
)
def test_numpy_quantile(
        dtype_and_a,
        dtype_and_q,
        as_variable,
        with_out,
        num_positional_args,
        native_array,
        frontend,
        fn_tree,
        on_device,
        keep_dims,
):
    input_dtype, a, axis, axis_excess = dtype_and_a
    input_dtype, q, axis, axis_excess = dtype_and_q
    if isinstance(axis, tuple):
        axis = axis[0]

    np_frontend_helpers.test_frontend_function(
        input_dtypes=input_dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        num_positional_args=num_positional_args,
        native_array_flags=native_array,
        frontend=frontend,
        fn_tree=fn_tree,
        on_device=on_device,
        a=a[0],
        q=q[0],
        axis=axis,
        out=None,
        keepdims=keep_dims,
        interpolation='linear'
    )
