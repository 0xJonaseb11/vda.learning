import plotly.express as px
import plotly.offline as opy
import plotly.graph_objects as go

import pandas as pd


def frequency_table(df):
    """Summarize selling price by manufacturer."""
    summary = (
        df.groupby("manufacturer", as_index=False)["selling_price"]
        .sum()
        .rename(
            columns={
                "manufacturer": "Manufacturer",
                "selling_price": "Total Selling Price",
            }
        )
    )

    table_html = summary.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format="%.2f",
        index=False,
        justify="center",
    )
    return table_html
