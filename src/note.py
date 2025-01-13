import marimo

__generated_with = "0.10.12"
app = marimo.App(width="full", app_title="Recommendation-Engine")


@app.cell
def _(mo):
    mo.md(r"""# **Read Data From S3**""")
    return


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
    load_dotenv("./.env")
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


@app.cell
def _(mo):
    mo.md(r"""# **Overview of maruti's data in Amazone S3**""")
    return


@app.cell
def _(mo):
    mo.md("""## *Loyalty Transaction Data*""")
    return


@app.cell
def _(pl):
    # Read data form CSV
    loyality = pl.read_csv(
        "./data/GD_LOYALTY_TRANS_T_P1.csv", infer_schema_length=100_000
    )

    # Diplay Data
    loyality
    return (loyality,)


@app.cell
def _(mo):
    mo.md(r"""## *SVOC*""")
    return


@app.cell
def _(pl):
    # Read data form CSV
    svoc = pl.read_csv(r"./data/GM_SVOV_T_P1.csv", infer_schema_length=100_000)

    # Diplay Data
    svoc
    return (svoc,)


@app.cell
def _(mo):
    mo.md(r"""## *MWAR*""")
    return


@app.cell
def _(pl):
    # Read data form CSV
    mwar = pl.read_csv(r"./data/MWAR_EXTE_T_P1.csv", infer_schema_length=100_000)

    # Diplay Data
    mwar
    return (mwar,)


@app.cell
def _(mo):
    mo.md(r"""## *Invoice Table*""")
    return


@app.cell
def _(pl):
    # Read data form CSV
    invoice = pl.read_csv(
        r"./data/SH_INVOICE_T_P1.csv", infer_schema_length=1_000_000
    )

    # Diplay Data
    invoice
    return (invoice,)


@app.cell
def _(mo):
    mo.md(r"""## *Add-On*""")
    return


@app.cell
def _(pl):
    # Read data form CSV
    addon = pl.read_csv(r"./data/VT_ADDON_T_P1.csv", infer_schema_length=1_000_000)

    # Diplay Data
    addon
    return (addon,)


if __name__ == "__main__":
    app.run()
