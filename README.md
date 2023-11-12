# ariadne-pydantic-class-on-scalar

Reproduction of issue when scalars used by `ariadne-codegen` points to a type
that has a field annotated with another class not yet loaded.

The issue is well known in Pydantic as
[Rebuild model
schema](https://docs.pydantic.dev/latest/concepts/models/#rebuild-model-schema)
which is to be used after we guarantee we loaded all classes. `ariadne-codegen`
does this unconditionally in all generated query/mutation/fragment files after
setting up the types.

In this example, the reference is:

`get_q1.GetQ1Q1` -> `scalars.AoB` -> `variants.A` -> `other.C`

`C` is not loaded or in scope when we import `GetQ1Q1` so we will get
[pydantic.errors.PydanticUndefinedAnnotation](https://docs.pydantic.dev/2.4/errors/usage_errors/#undefined-annotation).

```sh
    raise PydanticUndefinedAnnotation.from_name_error(e) from e
pydantic.errors.PydanticUndefinedAnnotation: name 'C' is not defined

For further information visit https://errors.pydantic.dev/2.4/u/undefined-annotation
```

Reproduce by running `poetry run python example/example.py`

## Pydantic only

This is an issue with how Pydantic work and it's possible to recreate the
issue with Pydantic only in a smaller example which is in the
[`pydantic_only`](pydantic_only) directory.

However, this one is a bit easier to solve by simply adding this in
[`a.py`](pydantic_only/a.py):

```python
from c import C
```

Reproduce by running `poetry run python pydantic_only/a.py`
