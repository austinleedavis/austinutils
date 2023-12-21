from setuptools import setup

setup(
    packages=["austin"],
    description="Austin's personal utils - you're welcome to use, but this is very badly maintained and commented!.",
    install_requires=[
        "einops",
        "numpy",
        "torch",
        "datasets",
        "transformers",
        "tqdm",
        "pandas",
        "datasets",
        "wandb",
        "fancy_einsum",
        "plotly",
        "rich",
        "matplotlib",
        "transformer_lens",
        "statsmodels"
    ],
    dependency_links=[
        'git+https://github.com/austinleedavis/austinutils.',
    ]
)
