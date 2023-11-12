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

## Potential fixes

So far I've found 2 alternative solutions.

### Use Pydantic's `BaseModel`

Instead of using `dataclass` classes it would be fixed by using Pydantic's
`BaseModel` instead. Of course I would still need to import the class for it to
be known and cannot put it behind `TYPE_CHECKING`.

`poetry run python fix_1/a.py`

### Import `C` wherever `B` is referred

By ensuring `C` is in scope wherever `B` is being used also seems to fix the
issue. This might be suitable for some projects but since this stems from using
`ariadne-codegen` that would be in every file in
[`grpahql_client`](example/graphql_client) that references `B` which in my case
is a lot (and in generated code outside my control).

`poetry run python fix_2/a.py`
