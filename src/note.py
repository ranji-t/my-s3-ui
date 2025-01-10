import marimo

__generated_with = "0.10.10"
app = marimo.App(width="medium")


@app.cell
def _():
    # Standard Imports
    import os

    # Third Party Imports
    import boto3
    import marimo as mo
    import polars as pl
    from dotenv import load_dotenv

    return boto3, load_dotenv, mo, os, pl


@app.cell
def _(load_dotenv):
    # Load .env files
    load_dotenv("../.env")
    return


@app.cell
def _(boto3, os):
    # Get The s3 resource
    s3 = boto3.resource(
        service_name="s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECTET_ACCESS_KEY"),
    )

    # Create Bucket
    bucket = s3.Bucket(os.getenv("BUCKET_NAME"))

    # List of objects
    keys = [obj.key for obj in bucket.objects.all()]

    # Display objects
    keys
    return bucket, keys, s3


if __name__ == "__main__":
    app.run()
