import argparse

from . import linear_regression

IMPLEMENTED_MODELS = ["linear_regression"]

def cli():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--year",
        default=2022,
        help="Year of the data."
    )
    
    parser.add_argument(
        "--month",
        default=1,
        help="Month of the data."
    )
    
    parser.add_argument(
        "--model",
        default="linear_regression",
        help=f"Kind of model to train, separated by `_`. Implemented models: {IMPLEMENTED_MODELS}"
    )
    
    return parser.parse_args()



if __name__ == "__main__":
    args = cli()
    year = int(args.year)
    month = int(args.month)
    model_name = args.model
    
    if model_name not in IMPLEMENTED_MODELS:
        raise NotImplementedError(f"{model_name} not implemented")
    
    if model_name == "linear_regression":
        model, features = linear_regression.train_and_valid(year, month)
        
    