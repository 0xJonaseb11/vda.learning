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
        classes="table table-hover table-sm mb-0",
        float_format="%.2f",
        index=False,
        justify="center",
    )
    return table_html


def visualizing_sales_with_sunburst_chart(df, height=600):
    """Generates a sunburst chart of sales by manufacturer, fuel, and body type."""
    fig = px.sunburst(
        df,
        path=["manufacturer", "fuel_type", "body_type"],
        values="selling_price",
        color="selling_price",
        color_continuous_scale="RdBu",
    )
    fig.update_traces(textinfo="label+value")
    fig.update_layout(
        height=height,
        margin=dict(t=0, l=0, r=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return opy.plot(fig, output_type="div", include_plotlyjs=False)


def visualizing_price_distribution(df):
    """Generates a histogram showcasing the distribution of vehicle selling prices."""
    fig = px.histogram(
        df,
        x="selling_price",
        nbins=50,
        labels={"selling_price": "Selling Price ($)"},
        color_discrete_sequence=["#636EFA"],
        opacity=0.8,
    )
    fig.update_layout(
        margin=dict(t=20, l=20, r=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Price Range",
        yaxis_title="Count",
    )
    return opy.plot(fig, output_type="div", include_plotlyjs=False)


def visualizing_manufacturer_shares(df):
    """Generates a donut chart of vehicle counts per manufacturer."""
    counts = df["manufacturer"].value_counts().reset_index()
    counts.columns = ["manufacturer", "count"]
    fig = px.pie(
        counts,
        values="count",
        names="manufacturer",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    fig.update_layout(
        margin=dict(t=20, l=20, r=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return opy.plot(fig, output_type="div", include_plotlyjs=False)


def visualizing_category_counts_bar_chart(df):
    """Generates a bar chart showing counts for various vehicle categories."""
    # We'll use Body Type as the primary category
    counts = df["body_type"].value_counts().reset_index()
    counts.columns = ["Category", "Count"]
    fig = px.bar(
        counts,
        x="Category",
        y="Count",
        color="Count",
        color_continuous_scale="Viridis",
        labels={"Count": "Number of Vehicles"},
        text_auto=True,
    )
    fig.update_layout(
        margin=dict(t=20, l=20, r=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Body Type",
        yaxis_title="Count",
    )
    return opy.plot(fig, output_type="div", include_plotlyjs=False)
